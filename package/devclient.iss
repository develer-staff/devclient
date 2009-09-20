; Copyright (C) 2009 Gianni Valdambrini, Develer S.r.l (http://www.develer.com)
;
; This program is free software: you can redistribute it and/or modify
; it under the terms of the GNU General Public License as published by
; the Free Software Foundation, either version 2 of the License, or
; (at your option) any later version.
;
; This program is distributed in the hope that it will be useful,
; but WITHOUT ANY WARRANTY; without even the implied warranty of
; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
; GNU General Public License for more details.
;
; You should have received a copy of the GNU General Public License
; along with this program.  If not, see <http://www.gnu.org/licenses/>.
;
; Author: Gianni Valdambrini gvaldambrini@develer.com


; The base url for download all files (without the trailing slash)
#define BASE_URL "http://devclient.develer.com/download"

; The include for the itd_* functions (used to add download functionalities)
#include <it_download.iss>


[Setup]
AppId={{2AFF7E77-E12D-42F7-880D-A52E2372B3E8}
AppName=DevClient
AppVerName=DevClient
AppPublisher=Develer s.r.l.
AppPublisherURL=http://devclient.develer.com
AppSupportURL=http://devclient.develer.com
AppUpdatesURL=http://devclient.develer.com
DefaultDirName={pf}\devclient
DefaultGroupName=DevClient
AllowNoIcons=yes
OutputBaseFilename=DevClient-Setup
OutputDir=.
SolidCompression=yes
Compression=lzma
WizardImageFile=compiler:WizModernImage-IS.bmp
WizardSmallImageFile=compiler:WizModernSmallImage-IS.bmp

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "italian"; MessagesFile: "compiler:Languages\Italian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "..\devclient.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\src\devclient\startcore.exe"; DestDir: "{app}\src\devclient"; Flags: ignoreversion
Source: "..\update\startupdater.exe"; DestDir: "{app}\update"; Flags: ignoreversion
Source: "..\update\startupdater.pkg"; DestDir: "{app}\update"; Flags: ignoreversion
Source: "..\update\updater.py"; DestDir: "{app}\update"; Flags: ignoreversion
Source: "..\update\updater.cfg"; DestDir: "{app}\update"; Flags: ignoreversion

[Icons]
Name: "{group}\DevClient"; Filename: "{app}\devclient.exe"
Name: "{group}\Uninstall DevClient"; Filename: "{uninstallexe}"
Name: "{commondesktop}\DevClient"; Filename: "{app}\devclient.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\DevClient"; Filename: "{app}\devclient.exe"; Tasks: quicklaunchicon

[Messages]
english.ReadyLabel2a=Click Install to continue with the installation, or click Back if you want to review or change any settings.%n%nATTENTION PLEASE: The task can take some minutes and require an internet connection.
italian.ReadyLabel2a=Premere Installa per continuare con l'installazione, o Indietro per rivedere o modificare le impostazioni.%n%nATTENZIONE: La procedura può durare alcuni minuti e richiede una connessione a internet.

[Run]
Filename: "{app}\devclient.exe"; Description: "{cm:LaunchProgram,DevClient}"; Flags: nowait postinstall skipifsilent

[Code]

// In order to make the update procedure most explicit, the first download of the updates are done here.

procedure InitializeWizard();
begin
  itd_init();
end;

procedure CurStepChanged(CurStep : TSetupStep);
var
  errorCode : Integer;
  tmpDir : String;
  updateDir : String;
begin
  // We have to wait after the installation because before, the {app} dir doesn't exists.
  if CurStep = ssPostInstall then
  begin
    tmpDir := ExpandConstant('{tmp}');
    updateDir := ExpandConstant('{app}\update');
    
    // Move the archives in the update directory of the client, and run the updater in the '--source=local' modality
    RenameFile(tmpDir + '\devclient_packages.tar.bz2', updateDir + '\devclient_packages.tar.bz2');
    RenameFile(tmpDir + '\devclient.tar.bz2', updateDir + '\devclient.tar.bz2');
    ShellExec('open', updateDir + '\startupdater.exe', '--source=local', updateDir, SW_HIDE, ewWaitUntilTerminated, errorCode);
    DeleteFile(updateDir + '\devclient_packages.tar.bz2');
    DeleteFile(updateDir + '\devclient.tar.bz2');
    // Finally, update the local version files.
    RenameFile(tmpDir + '\devclient_packages.version', updateDir + '\packages.version');
    RenameFile(tmpDir + '\devclient.version', updateDir + '\devclient.version');
  end;
end;

function NextButtonClick(CurPageID : Integer): Boolean;
begin
  if CurPageID = wpReady then
  begin
    // We have to download in {tmp} because in the wpReady page the directory {app} doesn't exists.
    itd_addfile('{#BASE_URL}/devclient_packages.tar.bz2', ExpandConstant('{tmp}\') + 'devclient_packages.tar.bz2');
    itd_addfile('{#BASE_URL}/devclient_packages.version', ExpandConstant('{tmp}\') + 'devclient_packages.version');
    itd_addfile('{#BASE_URL}/devclient.tar.bz2', ExpandConstant('{tmp}\') + 'devclient.tar.bz2');
    itd_addfile('{#BASE_URL}/devclient.version', ExpandConstant('{tmp}\') + 'devclient.version');
    itd_downloadafter(wpReady);
  end;
  Result := True;
end;

// The standard procedure to remove safety the installation directory doesn't work with DevClient, because
// the DevClient setup is only a 'straightforward way' to obtain the last version of the client (so, only few files
// are put inside the setup, and only these can be removed by the standard uninstall).
// Thus, we remove by code the directory of installation but before we ask to the user for a confirmation
// (because the user can choose a directory like C:\Windows or something like that..).
procedure CurUninstallStepChanged(CurUninstallStep : TUninstallStep);
var question : String;
begin
  if CurUninstallStep = usUninstall then
  begin
    question := 'Do you want to delete the directory ';
    if ActiveLanguage() = 'italian' then
      question := 'Vuoi eliminare la directory ';

    if MsgBox(question + ExpandConstant('"{app}"?'), mbConfirmation, MB_YESNO) = IDYES then
      DelTree(ExpandConstant('{app}'), True, True, True);
  end;
end;
