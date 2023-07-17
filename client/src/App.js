import "./App.css"
import React, {useEffect, useState} from 'react'
import { io } from "socket.io-client";


function App() {

const [data, SetData] = useState([{}])

useEffect(() =>{
  fetch("/data").then(
    res => res.json()
  ).then(
    data =>{
      SetData(data)
      console.log(data)
    }
  )
  }, [])

const socket = io("localhost:5001/", {
  transports: ["websocket"],
  cors: {
    origin : "http://localhost:3000/",
  },
})

socket.on("connect", (data) =>{
  console.log(data)
})

socket.on("disconnect", (data)=>{
console.log(data)
})

socket.on("newData",(data)=>{
  console.log(data)  
  SetData(data)
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