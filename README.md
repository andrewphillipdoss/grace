# grace
a Django app built for a pre-employment test

The app can be viewed at:
https://project-for-josh.herokuapp.com/

There instructions were as follows:

Create a web portal called “GRACE” - that does the following -

Grace is a list of people, like an excel sheet in style and appearance. For our purposes we only
need a few folks, but build it with hundreds in mind.

“Select All” is an ability to select all people. There are also check boxes next to each person’s name for individual or multiple selections. 

“Types” - are A, B, C, D 

“Label” - are any words used as a label.

“Unique” – is a button. When clicked, it opens a modal for a time input. When a time is input, the time is captured in the cell. All times should be standard and easy to input. Not every person is eligible for a unique input. The eligible have the button, the ineligible don’t. Eligibility can be controlled in the backend. I don’t need to see it.

“Sandwiches – are a number 0 to anything. They’ll usually hang around 0, 1, 2, 3. Only the eligible have the number. 

“Stop” -  is a button. When clicked, it does the same thing as unique.

Above the grid, there must also two buttons.

These are “Unique” and “Stop”, but meant for bulk actions when several people are selected or all are selected.  It captures the inputted time in the many selected cells.
Create filters for this view so it can be easier on the user.

Unique, Sandwiches:
Unique is a time input. But it’s an input with internal logic. 
Your grid counts six hours and twelve minutes from whatever time is chosen as unique time. 
Let’s assume unique time is 7:00 am.
Grid has to know (without showing) six hours and twelve minutes later is 01:12 pm. If unique time changes, it always has to adjust for six hours and twelve minutes after.
Within this six-hour twelve minute window, all is well. If stop time is input, all is well. 
But – if stop time is input .01 of a second outside of the window, a sandwich is added. Sandwiched are added on 30 minute increments until a stop time is input. 
Anything from .01 seconds – 30 minutes over the six twelve adds a sandwich.
Anything from 30.01 minutes – 60 minutes adds a sandwich
Anything from 60.01 minutes – 90 minutes adds a sandwich.
And so on.
The sandwich count only stops if a stop time is input. The sandwich column should auto update as thirty-minute increments occur. 

Part 2:
Create a button that downloads a spreadsheet of the completed data table. It should be in excel or .csv format. 
It should resemble this: 

