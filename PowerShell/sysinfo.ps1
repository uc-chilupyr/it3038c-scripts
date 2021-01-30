function getIP{
(Get-NetIPAddress).IPv4Address | Select-String "192*"
}


write-host(getIP)
$IP = getIP
$Date = Get-Date
$PowerShellVersion = $Host.Version.Major
$BODY = "This machine's IP is $IP. 
User is $env:USERNAME. 
Hostname is $env:COMPUTERNAME. 
PowerShell Version is $PowerShellVersion. 
Today's date is $Date"

write-host($BODY)

Send-MailMessage -To "yashuchilupuri@gmail.com" -From "yashchilupuri@gmail.com" -Subject "IT3038c windows SysInfo" -Body $BODY -SmtpServer smtp.google.com -port 587 -UseSSL -Credential (Get-Credential)