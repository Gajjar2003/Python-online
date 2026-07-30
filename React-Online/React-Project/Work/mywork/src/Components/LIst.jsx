import React, { useState } from "react";

function LIst() {
  const [newname, setname] = useState("");
  const [newdate, setdate] = useState("");
  const [newadd, setadd] = useState([
    {
      name: "Buy Car",
      duedate: "11/08/2026",
    },
    {
      name: "Go To Temple",
      duedate: "12/08/2026",
    },
    {
      name: "Complete React Project",
      duedate: "15/08/2026",
    },
  ]);

  const additems = () => {
    const newarray = {
      name: newname,
      duedate: newdate,
    };

    setadd([...newadd, newarray]);

    setname("");
    setdate("");
  };

  const changename = (e) => {
    setname(e.target.value);
  };

  const changedate = (e) => {
    setdate(e.target.value);
  };

  // Delete Todo
  const deleteitem = (index) => {
  
    const newlist = newadd.filter(
      (item, itemIndex) => itemIndex !== index
    );

    setadd(newlist);
  };

  return (
    <div>
      <div className="container mt-5">
        <div className="card shadow-lg">
          <div className="card-header bg-primary text-white text-center">
            <h2 className="mb-0">To-Do List App</h2>
          </div>

          <div className="card-body">
            <div className="row g-3">
              <div className="col-md-5">
                <input
                  type="text"
                  placeholder="Enter Todo Here..."
                  className="form-control"
                  onChange={changename}
                  value={newname}
                />
              </div>

              <div className="col-md-4">
                <input
                  type="date"
                  className="form-control"
                  onChange={changedate}
                  value={newdate}
                />
              </div>

              <div className="col-md-3">
                <button className="btn btn-success w-100" onClick={additems}>
                  Add
                </button>
              </div>
            </div>

            <hr />

            {/* List */}
            <div className="list-group">
              {newadd.map((item, index) => (
                <div className="list-group-item" key={index}>
                  <div className="row align-items-center">
                    <div className="col-md-5">{item.name}</div>

                    <div className="col-md-4">{item.duedate}</div>

                    <div className="col-md-3 text-end">
                      <button className="btn btn-danger" onClick={deleteitem}>Delete</button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default LIst;
