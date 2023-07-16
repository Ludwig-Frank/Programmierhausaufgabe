import "./App.css"
import React, {useState} from 'react'
import { io } from "socket.io-client";


function App() {

const [data, SetData] = useState([{}])

const socket = io("localhost:5001/", {
  transports: ["websocket"],
  cors: {
    origin : "http://localhost:3000/",
  },
})

socket.on("connect", () =>{
  console.log("Connected")
})

socket.on("disconnect", ()=>{
console.log("Disconnected")
})

socket.on('newData',(data)=>{
    SetData(data),
    console.log(data)
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