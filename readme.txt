PLEASE SCROLL DOWN FOR ENGLISH VERSION
Hallo,
in diesem File gehe ich kurz darauf ein, was ich jetzt alles von der Aufgabe wie umgesetzt habe und wie ihr die Applikation dann testen könnt.

Architektur:
Das Projekt besteht hauptsächlich aus 2 Komponenten. Dem Backend-Server und der Fontend-Applikation. Der Server holt sich die 
Wordpress Artikel von der gewünschten URL und verarbeitet diese zu der Wordcountmap. Zusätzlich überprüft der Server, ob neue Artikel vorhanden sind, verarbeitet diese und sendet sie an die Frontend-Applikation.

Der Server ist mit dem Flask-Framework realisiert und startet eine Flask-App, welche die Daten an das Frontend sendet und eine API bereit stellt. (Warum die API erforderlich ist, wird später erklärt)
Der Server etabliert dabei einen Handshake für den WebSocket und sendet die anzuzeigenden Daten über diesen. Zusätzlich wird ein Daemon-Thread gestartet,
welcher parallel überprüft, ob neue Daten vorhanden sind. Sollte dies der Fall sein, werden die daten neu angefordert und verarbeitet.

Die Frontend-Applikation empfängt die vom Server gesendeten Daten und zeigt diese an. Zur Übersiht wird der Titel der Artikel groß und fett abgebildet und darunter wird dann die
Wordcountmap abgebildet

Probleme: 
Durch die Kombinatorik aus eventlet, flask-socketio, requests und dem Threading, können die Datenpakete nicht per Websocket übertragen werden. Dadurch werden die Daten nicht ohne neuzuladen aktualisiert.
Auf dieses Problem kann ich bei Fragen auch gern näher eingehen.
Gelöst habe ich das Problem dadurch, dass die Daten auch per flask-Server API verfügbar sind. Das Frontend fetcht sich diese nun beim starten der Applikation.
Die aktuellen daten können dann durch manuelles neuladen angezeigt werden.
Ich wollte dennoch diese Version einreichen, um zu zeigen, dass ich das grundsätzliche Konzept des WebSockets verstanden habe und diesen auch nutzen kann. (Der Handshake funktioniert soweit)

Übersicht über die Akzeptanzkriterien:
1. Das Backend ruft zyklisch (alle paar Sekunden) die Blogbeiträge von der Seite internate.org ab (die Seite wurde in Absprache auf www.thekey.academy geändert) - ERFÜLLT
2. Das Backend verarbeitet die Blogbeiträge zu einer einfachen Word Count Map - ERFÜLLT
3. Das Backend sendet nach der Verarbeitung die Map per WebSocket an das Frontend - theoretisch ERÜLLT, allerdings werden die Daten nicht ordnungsgemäß empfangen
4. Das Frontend zeigt die neuen Beiträge an und aktualisiert sich selbstständig neu bei neuen Daten - NICHT ERFÜLLT, die aktuellen Daten werden nur bei manuellem Neuladen angezeigt

Bonuspunkte:
1. Eventgetriebene Verarbeitung - NEIN
2. Seite aktualisiert nur bei neuen Daten - Wäre erfüllt, wenn die Daten korrekt übertragen werden würden
3. Microservice Architektur - Kann ich nicht zu 100% beurteilen. Ich würde sagen teilweise

Zusätzliches:
Unittests für zentrale Funktionalität
Server-Logging


