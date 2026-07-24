import React from "react";

function Todolist() {
  return (
    <div>
      <h1>Wel Come To-Do-LIst</h1>
      <h2>To-Do-App</h2>
      <br />
       
      <div class="container text-center">
        <div class="row">
          <div class="col">
            <input
              type="text"
              placeholder="Enter Todo Here..."
              style={{ backgroundColor: "white" }}
            />
          </div>
          <div class="col">
            <input type="date" />
          </div>
          <div class="col">
            <button type="button" class="btn btn-success w-50">
              Add
            </button>
          </div>
        </div>
      </div>
    <br />
       <div class="container text-center">
        <div class="row">
          <div class="col">
            PC
          </div>
          <div class="col">
          22/06/2026
          </div>
          <div class="col">
            <button type="button" class="btn btn-danger w-50">
              Delete
            </button>
          </div>
        </div>
      </div>
        <br />
       <div class="container text-center">
        <div class="row">
          <div class="col">
            Laptop
          </div>
          <div class="col">
            11/08/2025
          </div>
          <div class="col">
            <button type="button" class="btn btn-danger w-50">
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Todolist;
