# Coded by Sezer Yavuzer Bozkır <admin@sezerbozkir.com>
# Date: 18.06.2017

from mysql_datasource import Articles_Dev

should_delete_row_id = []


# Remove Empty rows
def empty_rows():
    for row in Articles_Dev.select().where((Articles_Dev.answer == "") | (Articles_Dev.question == "")):
        should_delete_row_id.append(row.id)


# Remove length less than 20 and not Null
def wrongly_crawl_data():
    for row in Articles_Dev.select():
        if 1 < len(row.answer) < 20 or 1 < len(row.question) < 20:
            should_delete_row_id.append(row.id)


# Remove rows function
def removed_rows():
    for rid in should_delete_row_id:
        Articles_Dev.delete().where(Articles_Dev.id == rid).execute()


# Only hold url data rows wrongly crawled. So should be remove.
def only_link_rows():
    for row in Articles_Dev.select():
        if row.answer.startswith("http") or row.question.startswith("http"):
            should_delete_row_id.append(row.id)


if __name__ == '__main__':
    empty_rows()
    only_link_rows()
    wrongly_crawl_data()
    removed_rows()
    print("{} rows removed.".format(len(should_delete_row_id)))
