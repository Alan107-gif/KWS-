# KWS-
chat systhem made out of python scripts.in the ChatDirektory you can find the programm to install,and in the ServerDirektory is a py script,that anyone can run on his host server,there can be more than one of these server scripts launched,beacouse they are decentralized and work together to sustain the chat programm,that the users use.based on kws. https://github.com/Alan107-gif/kws follow the link or you see it at the and of this letter.







> kws
>
> Kontakt-work-Station is a decentralized communication network like mobile towers.
> 
> KWS - Kommunikationsnetzwerk -OpenScource!
> 
> Beschreibung: KWS ist eine leichte, in Python implementierte Lösung für ein dezentrales Kommunikationsnetz. Das System stellt eine direkte, computer-zu-computer Verbindung her – ähnlich einem Mesh-Netzwerk. Es besteht aus drei Hauptkomponenten: •  >kws.py – der Server, der dauerhaft läuft, einen einzigartigen Auth-Key generiert und Konfigurations- sowie Kontaktdateien (contaktd.cdf) verwaltet. • kws-client.py – der Client, der periodisch Anfragen (z. B. INFO) an alle Kontakte sendet >undfehlgeschlagene Nachrichten in einer Datei (data.ksys) zwischenspeichert. • kws-service.py – eine Befehlszeilenschnittstelle, über die der Nutzer Kontakte hinzufügen, Nachrichten senden und Anfragen (z. B. ADDLIST, LIST) manuell auslösen kann.
>
> Vorteile: • Leichtgewichtig: Es werden nur systemeigene Bibliotheken (Sockets, Threading etc.) genutzt. • Dezentral: Jeder Rechner agiert als Knoten in einem Netzwerk, ohne zentrale Serverabhängigkeit. • Flexibel: Erweiterte Befehle ermöglichen das >Teilen von Kontaktlisten, selektives Hinzufügen von Kontakten und automatische Synchronisation. • Offline-Nachrichten: Nachrichten, die nicht sofort zugestellt werden können, werden zwischengespeichert und bei Wiederverbindung automatisch gesendet. • > Einfache Installation: Mit den beiliegenden Installationsskripten (instance-kws.sh für Linux, instance-kws.bat für Windows) wird ein ZIP-Paket heruntergeladen, entpackt und ein Autostart eingerichtet.
