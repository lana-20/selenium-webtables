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

Similarily, let's find the number of columns in the table. If I find the number of headers, that would equal the number of columns. The headers are in the 1st _tr_. I need to count the number of _th_ tags inside the 1st _tr_.

This Xpath returns 4 elements, which means there are 4 headers (because there are 4 columns):

	//table[@name='BookTable']/tbody/tr[1]/th

Again, I want to shorten the Xpath. I can remove the index from _tr_ because by default it goes to the 1st _tr_ in the BookTable.
	
	//table[@name='BookTable']//tr/th

With or without the index, it captures 4 elements:

	num_of_columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th"))

<img src="https://user-images.githubusercontent.com/70295997/206880559-5d1aad2e-1304-4e9d-a275-2509deba3dbb.png" width=600>

I've found the count of rows and columns. I'll use these values to read the data from the table.

Now, I want to read data from a specific row and column. Let's say I want to capture 'Master in Selenium'. It's  in the 5th _tr_ row, 1st _td_ column.

<img src="https://user-images.githubusercontent.com/70295997/208344980-34838eb0-7cd3-4287-972c-b3ebfe4d87cb.png" width=350>

Write an Xpath, pass in the row and column index number to get the right value:

	//table[@name='BookTable']/tbody/tr[5]/td[1]

<img src="https://user-images.githubusercontent.com/70295997/208758940-fb2c9d9f-6ee3-4ae9-8e5b-78c9cd59a423.png" width=600>

Similarily, to retrieve Subject Java, traverse to the 3rd row, 3rd column:

	//table[@name='BookTable']/tbody/tr[3]/td[3]

<img src="https://user-images.githubusercontent.com/70295997/208759503-046ee73e-cbaa-420c-acab-4b06b0c27225.png" width=600>

I've located the desired web element. And now want to extract its text value by using the _.text_ keyword and storeit in the variable _data_. To extract any specific value from the table, pass in the row and column numbers. The rest of the Xpath remains the same.

	data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text

Now I want to read data from all rows and columns. For that, I write two looping statements to find out how many rows and columns. One loop statement is for incrementing the rows, the other loop statement is for incrementing the columns. There are multiple columns per row. First, I focus on reading the 1st row columns, then move on to reading the 2nd row column fields and so on.

One for loop increments the rows. Inside it, I nest another for loop to read all the column data from a specific row.  There are 7 rows, but the 1st row is the header part, which I want to ignore. So, I start from the 2nd row. Inside the column loop I provide the Xpath with dynamic row and column values. This way, I parameterize the data inside the Xpath. I pass params/arguments into Xpath, which then becomes a dynamic Xpath. 

I want specify the _r_ variable for a row, and the _c_ value for a column number. But Xpath does not allow to specify variables as in _tr[r]/td[c]_. I have to follow a certain syntax to pass params into Xpath. Convert the params into a string format with the _str()_ function. Prefix and postfix the  _str()_ function with the the '+' plus operator as in _+str(r)+_ and put in quotes as in _"+str(r)+"_. Then only the values get passed into Xpath dynamically. This is the syntax to extract the variable and pass the data into the Xpath. I cannot pass the variables directly into the Xpath. 
To print the data in a tabulat format, add an empty line after a row with _print()_ and end each column value with some space.

	for r in range(2, num_of_rows + 1):
		for c in range(1, num_of_columns + 1):
			data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
			print(data, end="   ")
		print()

Now, I want to retrieve the data based on a certain condition. Let's say my requirement is to get the book names authored by Mukesh. The Author names are available in the 2nd column. I have to read the author name from each and every row or compare it with "Mukesh". 

<img src="https://user-images.githubusercontent.com/70295997/209004170-70577483-6c6b-44e2-b9bf-50e6b0ab4372.png" width=600>

If the author name matches "Mukesh", then from the same row get the value of the BookName and print it. If the author name is not equal to Mukesh, then go to the next name. This happens through the looping statement, beacause I need to read every author from every row in the table. I need only 2 columns - Author and BookName.

First, write the loop which repeats the number of rows, because I need to get all the author names one by one.
Xpath _//table[@name='BookTable']/tbody/tr/td_ slects all the rows and columns in the table. To read the 2nd column, pass the column index to the Xpath _//table[@name='BookTable']/tbody/tr/td[2]_. By changing the row numbers from _tr[2]_ to _tr[7]_, I can get all the authors one by one. But the column number remains constant, because at the moment I don't need any other columns. The column number can remain hard coded, but the row number has to change with every iteration.

<img src="https://user-images.githubusercontent.com/70295997/209004473-ee6e4bcc-37dc-4638-b5b0-5a14522da26c.png" width=400>

While the column number remains constant, I have to pass the _r_ value in lieu of the row index number. As soon the author name matches "Mukesh", I immediately capture the book name in the same row. I reuse the _author_name_ Xpath and change the column number to _td[1]_ to capture the name of the book.

Suppose I also want to print the price details along with the author and book name. Simply change the logic by adding the _price_ variable pointing to the 4th column _td[4]_.


	for r in range(2, num_of_rows + 1):
		author_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"])/td[2]").text
		if author_name == "Mukesh":
			book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"])/td[1]").text
			price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"])/td[4]").text
			print(book_name, "	", author_name, "		", price)

This is how I write the logic and retrieve the rows and columns data from a table.

There are also dynamic tables where data always changes, such as those in the OrangeHRM app (https://opensource-demo.orangehrmlive.com/).

Start with the login using username _Admin_ and password _admin123_. Then to navigate to a table, go to Admin tab > User Management > Users (https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers).
This table data consistently changes all the time, it's beyond my control. There are user names, user roles, employee names and status available in the table. Some user roles are Admin, some are ESS. Every user is in the Enabled state.

<img src="https://user-images.githubusercontent.com/70295997/209029374-69142c86-e994-4bd5-a1c7-f7e8fa379503.png" width=600>

Let's say my requirement is to find out how many users are in the Enabled status and how many Disabled. Currently, all of my users are Enabled. I'm going to turn some of them to Disabled for testing purposes.

<img src="https://user-images.githubusercontent.com/70295997/209029433-fb7c5d74-7a22-40c0-afd9-dec8a9b33131.png" width=600>

No need to work with all the rows and columns. I only need the Status column to find the number of Enabled and Disabled employees.

First, navigate to the table.

	# Admin -> User Management -> Users
	wait = driver.WebDriverWait(driver, 5)
	wait.until(EC.element_to_be_present((By.XPATH, "//li//a//span"))).click()   # Admin

	driver.find_element(By.XPATH, "//nav//li/span").click()   # User Management
	driver.find_element(By.CSS_SELECTOR, "a[role='menuitem']").click()  # Users

Then, find out the status of employees. I need to go through each row and capture the Status column value. From every row, I capture the 5th column value. I need to repeat this in every row, for that I capture the total number of rows via a looping statement.

Find the total number of rows available inside the table body, ignore the table headers.

	rows = len(driver.find_elements(By.XPATH, "//*[@class='oxd-table-body']/div/div"))
	print("total Number of rows:", rows)

<img src="https://user-images.githubusercontent.com/70295997/209053823-fc67052a-9809-4c85-be12-648c90bd31d7.png" width=600>

<img src="https://user-images.githubusercontent.com/70295997/209051626-c43e7cb7-2049-4619-a009-1243cccdf3e4.png" width=400>

To get each Status I have to dynamically pass the row number.

	count = 0
	for r in range(1, rows + 1):
		status = driver.find_element(By.XPATH, "//*[@class='oxd-table-body']/div["+str(r)+"]/div/div[5]")).text
		if status == "Enabled":
			count += 1

	print("Total number of users:", rows)
	print("Number of enabled users:", count)
	print("Number of disabled users:", (rows - count))

A typical table tag structure is:

<img src="https://user-images.githubusercontent.com/70295997/209053097-a81a60d5-d6db-4c63-8488-17a174ae8ea4.png" width=150>

Extra Practice: Print the user names and user roles if the user role is ESS.

	for r in range(1, rows + 1):
		role = driver.find_element(By.XPATH, "//*[@class='oxd-table-body']/div["+str(r)+"]/div/div[3]")).text
		username = driver.find_element(By.XPATH, "//*[@class='oxd-table-body']/div["+str(r)+"]/div/div[2]")).text
		if role == "ESS":
			print(username, role)
