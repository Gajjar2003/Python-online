import React from 'react'

function Clocktime() {

  const time = new Date()

  return (
    <div>
        <p className='lead'>This is  the current time {time.toDateString()} - {time.toLocaleTimeString()} </p>
    </div>
  )
}

export default Clocktime
