import React from 'react'

function LIst() {
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
          />
        </div>

        <div className="col-md-4">
          <input
            type="date"
            className="form-control"
          />
        </div>

        <div className="col-md-3">
          <button className="btn btn-success w-100">
            Add
          </button>
        </div>

      </div>

      <hr />

      <div className="list-group">

        <div className="list-group-item">
          <div className="row align-items-center">

            <div className="col-md-5">
              Buy Car
            </div>

            <div className="col-md-4">
              11/08/2026
            </div>

            <div className="col-md-3 text-end">
              <button className="btn btn-danger">
                Delete
              </button>
            </div>

          </div>
        </div>

      </div>

    </div>

  </div>
</div>
    </div>
  )
}

export default LIst
