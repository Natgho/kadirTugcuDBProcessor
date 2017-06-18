# Coded by Sezer Yavuzer Bozkır <admin@sezerbozkir.com>
# Date: 18.06.2017

from mysql_datasource import Articles_Dev

should_delete_row_id = []


def empty_rows():
    for row in Articles_Dev.select().where((Articles_Dev.answer == "") | (Articles_Dev.question == "")).limit(1):
        should_delete_row_id.append(row.id)


def wrongly_crawl_data():
    for row in Articles_Dev.select().limit(60):
        if 1 < len(row.answer) < 20 or 1 < len(row.question) < 20:
            print(row.id)


def removed_rows():
    for rid in should_delete_row_id:
        Articles_Dev.delete().where(Articles_Dev.id == rid).execute()

def only_link_rows():
    for row in Articles_Dev.select().limit(100):
        if row.answer.startswith("http") or row.question.startswith("http"):
            print(row.id)


if __name__ == '__main__':
    empty_rows()
    only_link_rows()
    # wrongly_crawl_data()
    # removed_rows()
    print(should_delete_row_id)
