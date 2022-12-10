# Selenium Webtables

Sometimes in the app I encounter data in a tabular format. I can perform various types of operations on the __WebTables__, a.k.a. HTML tables.

There are 2 WebTable types:
1) __Static WebTable__ displays the same data any time I open the table. 
2) __Dynamic WebTable__ displays different data at different times. The data keeps dynamically updating.

What is a WebTable? How does it work with my app? What are the different tags available for the Webtable? How to represent rows, columns, headers, data and other things in the table? Let's find out.

Go to https://testautomationpractice.blogspot.com/. Scroll down to work on the HTML table.

<img src="https://user-images.githubusercontent.com/70295997/206872438-a8d45af8-ea88-409d-b215-c94d68b4c414.png" width=600></img>

It's a table that contains various book names. authors, subject, and price. The data is aligned in the table. I want to perform different operations on this table, eg, count the number of rows or columns in a table, read a specific row data, or read a specific row and column data from the cell, read all the rows or all the columns. Or, based on a certan condition, I may want to retrieve the data from the table.

The tag names available for the table is _table_. It has an attribute called 'name' with the value "BookTable". Sometimes, a table tag has no attributes at all, just the tag name. Inside the _table_ tag, there's the _tbody_ representing the whole body of the table.

<img src="https://user-images.githubusercontent.com/70295997/206873000-608f5050-aa4a-4dbd-878d-0a7befac0334.png" width=600>

If I expand the _tbody_ tag, I can see a lot of _tr_ tags in it. There are multiple 'tr's, each representing a table row.
<img src="https://user-images.githubusercontent.com/70295997/206878522-801b7a57-94aa-4336-a54e-5c527e99b0fb.png" width=600>

When I move my cursor on a _tr_, it highlight the corresponding row in the table. Each _tr_ represents one entire row.

If I expand the 1st _tr_, I can see the _th_ tag which stands for the table header. The 1st row contains the table headers.
<img src="https://user-images.githubusercontent.com/70295997/206878713-2bebf4d4-1b82-4245-8657-8ae4ac685177.png" width=600>

The 1tr containts 5 _th_ tags, each representing a header in a particular table.
