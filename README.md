# OMEGALIB - daHandles module 

The daHandles library contains re-usable code modules to support the implementation of on-screen handles for direct manipulation of 3D objects within the Data Arena. It relies on *omegalib* and *cyclops*.

## Overview

This library includes support for the following features and functionality:

 - Reusable abstractions for different types of cursor, control or groups of controls
 - Customisable on-screen control appearance and geometry
 - Configurable selection manager, which is able to track independent selections for each cursor in the environment

The library includes some basic example controls and control groups, which you may use in your applications, or as examples to guide the development and addition of new controls to the library:

 - A simple 'whisker' control supporting customizable control geometry which may be used as a building block for the implementation of more complex control groups.
 - A simple tri-axis control group, for manipulating objects in 3D space.
 - Individual scale, rotate, and translate example control groups.
 - A more complex transform control group, which supports multiple operations depending on the selected mode.

## How To Use

Please see the following tutorial for further information:

http://www.dataarena.net/all_tutorials/omigalib-tutorial/advanced-omegalibosg-applications/on-screen-handles/