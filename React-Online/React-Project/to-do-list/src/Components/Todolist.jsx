import React from "react";
import { useState } from "react";

function Todolist(props) {

  const [newlist,setlistt] = useState()
  

  const addbutton =(e)=>{
    //console.log(e);
    console.log(e.target.value);

  
    
    
  }

  

  return (
    <div>
      <h1>Wel Come To-Do-LIst</h1>
      <h2>To-Do-App</h2>
      <br />

      <div className="container text-center">
        <div className="row">
          <div className="col">
            <input
              type="text"
              placeholder="Enter Todo Here..."
              style={{ backgroundColor: "white" , color :"black"}}
            />
          </div>
          <div className="col">
            <input type="date" />
          </div>
          <div className="col">
            <button type="button" className="btn btn-success w-50" value="addlist" onClick={addbutton}>
              Add
            </button>
          </div>
        </div>
      </div>
      <br />

      <div className="container text-center">
        {props.itemslist.map((abc) => (
          <div className="row"key={abc.name} >
            <div className="col" >{abc.name}</div>
            <div className="col"  >{abc.duedate}</div>
            <div className="col"><br />
              <button type="button" className="btn btn-danger w-50">
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Todolist;
