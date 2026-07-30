import React, { useState } from "react";

function EmployeeTodo() {

  const [newname, setname] = useState("");
  const [newdept, setdept] = useState("");
  const [newtake, settake] = useState("");
  const [newdate, setdate] = useState("");

  const [newemployee, setemployee] = useState([
    {
      name: "Jenil",
      dept: "IT",
      take: "Complete React Project",
      duedate: "2026-08-11",
    },
    {
      name: "Meet",
      dept: "HR",
      take: "Complete Django Task",
      duedate: "2026-08-12",
    },
    {
      name: "Vraj",
      dept: "Development",
      take: "Prepare Presentation",
      duedate: "2026-08-15",
    },
    {
      name: "Om",
      dept: "Testing",
      take: "Test Website",
      duedate: "2026-08-20",
    },
  ]);


  const changename = (e) => {
    setname(e.target.value);
  };

 
  const changdept = (e) => {
    setdept(e.target.value);
  };

  const changetake = (e) => {
    settake(e.target.value);
  };

  const changedate = (e) => {
    setdate(e.target.value);
  };


  const addemployee = () => {
   

    const newarray = {
      name: newname,
      dept: newdept,
      take: newtake,
      duedate: newdate,
    };

    setemployee([...newemployee, newarray]);

   
    setname("");
    setdept("");
    settake("");
    setdate("");
  };

 
  const deleteemployee = (deleteIndex) => {
    const newlist = newemployee.filter(
      (item, index) => index !== deleteIndex
    );

    setemployee(newlist);
  };

  return (
    <div className="container mt-5">
      <div className="card shadow-lg">

       
        <div className="card-header bg-primary text-white text-center">
          <h2 className="mb-0">Employee To-Do List</h2>
        </div>

        <div className="card-body">

      
          <div className="row g-3 mb-4">

       
            <div className="col-md-3">
              <input
                type="text"
                className="form-control"
                placeholder="Employee Name"
                onChange={changename}
                value={newname}
              />
            </div>

          
            <div className="col-md-3">
              <input
                type="text"
                className="form-control"
                placeholder="Department"
                onChange={changdept}
                value={newdept}
              />
            </div>

           
            <div className="col-md-3">
              <input
                type="text"
                className="form-control"
                placeholder="Enter Task"
                onChange={changetake}
                value={newtake}
              />
            </div>

         
            <div className="col-md-2">
              <input
                type="date"
                className="form-control"
                onChange={changedate}
                value={newdate}
              />
            </div>

          
            <div className="col-md-1">
              <button
                className="btn btn-success w-100"
                onClick={addemployee}
              >
                Add
              </button>
            </div>

          </div>

        
          <div className="table-responsive">
            <table className="table table-bordered table-hover text-center align-middle">

              <thead className="table-dark">
                <tr>
                  <th>#</th>
                  <th>Employee Name</th>
                  <th>Department</th>
                  <th>Task</th>
                  <th>Due Date</th>
                  <th>Status</th>
                  <th>Action</th>
                </tr>
              </thead>

              <tbody>

                {newemployee.map((item, index) => (
                  <tr key={index}>

                    <td>{index + 1}</td>

                    <td>{item.name}</td>

                    <td>{item.dept}</td>

                    <td>{item.take}</td>

                    <td>{item.duedate}</td>

                    <td>
                      <span className="badge bg-warning">
                        Pending
                      </span>
                    </td>

                    <td>
                      <button
                        className="btn btn-danger btn-sm"
                        onClick={() => deleteemployee(index)}
                      >
                        Delete
                      </button>
                    </td>

                  </tr>
                ))}

              </tbody>

            </table>
          </div>

        </div>

 
        <div className="card-footer text-center">
          <strong>
            Total Tasks: {newemployee.length}
          </strong>
        </div>

      </div>
    </div>
  );
}

export default EmployeeTodo;