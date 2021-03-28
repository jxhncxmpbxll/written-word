import React, { useState, useEffect } from 'react';

import styles from './styles/inputURL.css';

const InputURL = ({ handleURLInput, handleShowProgress }) => {
  return (
    <div className={styles.inputContainer}>
      <input
      className={styles.inputStyle}
      type="text"
      placeholder="Input URL"
      onChange={(text)=> handleURLInput(text)}/>
      <button
        className={styles.transcribeButtonStyle}
        onClick={()=> handleShowProgress()}
        type="button">TRANSCRIBE</button>
    </div>
  )
}

export default InputURL;