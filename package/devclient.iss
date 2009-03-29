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
OutputBaseFilename=DevClient Setup
Compression=lzma
SolidCompression=yes

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
Filename: "{app}\update\startupdater.exe"; Flags: runhidden
Filename: "{app}\devclient.exe"; Description: "{cm:LaunchProgram,DevClient}"; Flags: nowait postinstall skipifsilent

