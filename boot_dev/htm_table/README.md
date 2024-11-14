# HTML Table

Doc2Doc should have tools to create HTML boilerplate. One of the features should create a table. An HTML table has a header row and data rows. A header row has headers for the columns. Each normal row has data cells which contain the information in the table. It is essentially a 2-dimensional list.

Example HTML Table:

```
<table>
  <tr>
    <th>Row 1, Header 1</th>
    <th>Row 1, Header 2</th>
  </tr>
  <tr>
    <td>Row 2, Cell 1</td>
    <td>Row 2, Cell 2</td>
  </tr>
  <tr>
    <td>Row 3, Cell 1</td>
    <td>Row 3, Cell 2</td>
  </tr>
</table>

```

"td": Each item in a table goes in its own data cell, which are arranged in rows.
"tr": The table row tag goes around each row of cells.
"th": The header cells hold the headers for each column and belong in the first row.
"table": This is the parent tag of the entire table.
Result:

Row 1, Header 1	Row 1, Header 2
Row 2, Cell 1	Row 2, Cell 2
Row 3, Cell 1	Row 3, Cell 2
Assignment
Complete the create_html_table function. It takes a list of lists of strings, data_rows, and returns a function, create_table_headers. create_table_headers should take a list of strings, headers, and convert them into the header row of the table, then return the complete HTML table as a string without any added whitespace or indentation.

Use the provided functions to complete the create_html_table function:

Use the accumulators and the map function to convert the data_rows into a single string of html rows.
Use map to convert each string in the data_rows list into data cells within a table row.
Accumulate the table rows together as a single string.
Within the create_table_headers function:
Access the nonlocal rows string.
Accumulate the strings in the headers list as header cells in a single table row.
Add the row of headers to the beginning of the rows string.
Add the final tag, "table", around all of the rows.
Return one single string containing the HTML table.
