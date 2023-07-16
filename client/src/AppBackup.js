import React, {useEffect,useState} from 'react'
import { io } from "socket.io-client";


const socketio = io("localhost:5003/", {
  transports: ["websocket"],
  cors: {
    origin: "http://localhost:3000/",
  },
});

io.listen(5003)

const [data, SetData] = useState([{}])

function App() {

const [data, SetData] = useState([{}])

socketio.on("newData", (newData)=>{
  console.log("Daten empfangen")
  SetData(newData)
  })
  
  return (

    <div>
    {(typeof data.wordcountmap === `undefined`) ? (
        <p>Loading...</p>
    ) : (
      typeof data.wordcountmap === 'string')? (
        <p> {data.wordcountmap} </p>
      ) : (
        data.wordcountmap.map((member, i) => (
            member.map((element,j) => (
                (typeof element == "string") ?(
                    <h1 key = {j} style = {{fontsize:30}}>{element}</h1>
                ) : (
                    element.map((content,k) => (
                        <p key = {k}>{content}</p>
                    )
                    )
                )
                 

            ))
         ))
    )}
</div>
  )
}

export default App