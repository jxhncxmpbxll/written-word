import React from "react";

const ProgressBar = (props) => {
  const { color, progress } = props;

  const barContainerStyle = {
    height: '25px',
    width: '100%',
    backgroundColor: "#e0e0de",
    textAlign: 'center'
  }

  const fillBarStyle = {
    height: '100%',
    width: `${progress}%`,
    backgroundColor: color,
  }

  const percentageStyle = {
    padding: '5px',
    color: 'white',
    fontWeight: 'bold',
  }

  return (
    <div style={barContainerStyle}>
      <div style={fillBarStyle}>
        <span style={percentageStyle}>{`${progress}%`}</span>
      </div>
    </div>
  )
}

export default ProgressBar;