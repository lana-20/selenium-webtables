# Selenium WebTables

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

The 1tr containts 4 _th_ tags, each representing a header in a particular table.

The actual data starts from the 2nd _tr_. Now, I expand the 2nd _tr_ and see multiple _td_ tags, which stand for table data. From the 2nd _tr_ onward, the _td_ tags with the actual table data are available. Data is inserted inside the table data tags.
<img src="https://user-images.githubusercontent.com/70295997/206879456-4a494489-d158-47ca-989f-4fcd154dfd5a.png" width=600>

This is the structure of the table in HTML.

Mostly, I work with customized Xpaths to work with the data in the table. Inside the Xpath I can dynamically pass a parameter. I call this a dynamic Xpath.

Perform a few operations on the table:
1) Count the number of rows and columns
2) Read a specific row and column data
3) Read all the rows and columns data
4) Read data based on a condition. Eg, list the book names whose author is Mukesh. There are 2 books written by Mukesh, I want to retrieve only those. So, I do a condition-based retrieval of the data.

<img src="https://user-images.githubusercontent.com/70295997/206879836-4d4d9828-f008-42ad-913d-6859d21cfc54.png" width=600>

To count the number of rows, I can simply count the number of 'tr's. Every _tr_ tag represents one web element. I can capture all the _tr_ tags and count how many are there. This would equal to the number of rows.

Write one Xpath which matches/points to all the 'tr's from the table:

	//table[@name='BookTable']/tbody/tr


Point to the 1st row:


	//table[@name='BookTable']/tbody/tr[1]


Point to the 2nd row:


	//table[@name='BookTable']/tbody/tr[2]

By changing the index numbers, I can point to all the different rows, all the way up to tr[7]. I can shorten the syntax, by removing the _tbody_ tag:

	//table[@name='BookTable']//tr

This returns all the 'tr's, i.e. multiple web elements:

	driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")

But I don't need all the elements, I just need the count. For that, I use the _len()_ function:

	len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))

I store the count value in a variable called num_of_rows:

	num_of_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))

Similarily, let's find the number of columns in the table.
