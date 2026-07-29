import React, { useState } from "react";

function Todolist() {
  const todolist = [
    {
      name: "Buy Car",
      duedate: "11/08/2026",
    },
    {
      name: "Go to Temple",
      duedate: "12/08/2026",
    },
    {
      name: "Rain For today",
      duedate: "24/07/2026",
    },
    {
      name: "Water level is high",
      duedate: "12/08/2026",
    },
  ];

 
  const [newlist, setlistt] = useState(todolist);

  const [newname, setname] = useState("");
  const [newdate, setdate] = useState("");

  const addbutton = () => {
  

    const newitem = {
      name: newname,
      duedate: newdate,
    };

   
    setlistt([...newlist, newitem]);


    setname("");
    setdate("");
  };

  const changename = (e) => {
    setname(e.target.value);
  };

  const chnagedate = (e) => {
    setdate(e.target.value);
  };


  const itemsdelete = (index) => {
    const newarray = newlist.filter((item, itemIndex) => {
      return itemIndex !== index;
    });

    setlistt(newarray);
  };

  return (
    <div>
      <h1>Welcome To-Do-List</h1>
      <h2>To-Do-App</h2>

      <br />

      <div className="container text-center">
        <div className="row">

          <div className="col">
            <input
              type="text"
              placeholder="Enter Todo Here..."
              className="form-control"
              onChange={changename}
              value={newname}
            />
          </div>

          <div className="col">
            <input
              type="date"
              className="form-control"
              onChange={chnagedate}
              value={newdate}
            />
          </div>

          <div className="col">
            <button
              type="button"
              className="btn btn-success w-50"
              onClick={addbutton}
            >
              Add
            </button>
          </div>

        </div>
      </div>

      <br />

      <div className="container text-center">
        {newlist.map((abc, index) => (
          <div className="row" key={index}>

            <div className="col">
              {abc.name}
            </div>

            <div className="col" type="date">
              {abc.duedate}
            </div>

            <div className="col"><br />
              <button
                type="button"
                className="btn btn-danger w-50"
                onClick={() => itemsdelete(index)}>
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