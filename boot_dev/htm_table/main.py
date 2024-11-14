from functools import reduce


def create_tagged(tag):

    def tagged(content):
        return f"<{tag}>{content}</{tag}>"

    return tagged


def create_accumulator(tagged):

    def accumulate(items):
        return reduce(lambda acc, item: acc + tagged(item), items, "")

    return accumulate


tag_data = create_tagged("td")
tag_header = create_tagged("th")
tag_row = create_tagged("tr")
tag_table = create_tagged("table")

accumulate_data_cells = create_accumulator(tag_data)
accumulate_rows = create_accumulator(tag_row)
accumulate_headers = create_accumulator(tag_header)


def create_html_table(data_rows):
    rows = accumulate_rows(map(accumulate_data_cells, data_rows))

    def create_table_headers(headers):
        nonlocal rows

        header_row = tag_row(accumulate_headers(headers))
        rows = header_row + rows

        return tag_table(rows)

    return create_table_headers
