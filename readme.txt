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

ENGLISH VERSION

Hello,
in this file I briefly go into what I have now implemented everything from the task how and how you can then test the application.

Architecture:
The project consists mainly of 2 components. The backend server and the fontend application. The server fetches the 
Wordpress articles from the desired URL and processes them to the wordcountmap. Additionally, the server checks for new articles, processes them and sends them to the frontend application.

The server is implemented with the Flask framework and launches a Flask app that sends the data to the frontend and provides an API. (Why the API is needed will be explained later).
The server thereby establishes a handshake for the WebSocket and sends the data to be displayed over it. Additionally a daemon thread is started,
which checks in parallel if new data is available. If this is the case, the data is requested and processed again.

The frontend application receives the data sent by the server and displays it. For overview, the title of the article is displayed large and bold and below it is the
Wordcountmap is displayed

Problems: 
Due to the combinatorics of eventlet, flask-socketio, requests and the threading, the data packets cannot be transferred via websocket. Thus the data is not updated without reloading.
If you have any questions, I can go into this problem in more detail.
I solved the problem by making the data available via the flask server API. The frontend now fetches them when starting the application.
The current data can then be displayed by manually reloading.
I still wanted to submit this version to show that I understood the basic concept of WebSockets and can use it. (The handshake works so far)

Overview of acceptance criteria:
1. the backend cyclically (every few seconds) retrieves the blog posts from the internate.org page (the page has been changed to www.thekey.academy by agreement) - FULFILLED
2. the backend processes the blog posts to a simple word count map - FULFILLED
3. the backend sends the map via WebSocket to the frontend after processing - theoretically FULFILLED, but the data is not received properly
4. the frontend displays the new posts and refreshes itself on new data - NOT FULFILLED, the current data is only displayed when manually reloaded

Bonus points:
1. event driven processing - NO.
2. page refreshes only on new data - WOULD be fulfilled if data was transferred correctly
3. microservice architecture - Can't judge 100%. I would say partially

Additional:
Unittests for central functionality
Server logging

