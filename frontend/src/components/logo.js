import React from 'react';

import { logo } from '../icons/icons';
import styles from './styles/logo.css';

const Logo = () => {

  return (
    <div className={styles.logoContainer}>
      <h1>Written Word</h1>
      <div className={styles.iconContainer}>{logo}</div>
    </div>
  )
}

export default Logo;