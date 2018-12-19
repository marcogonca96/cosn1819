#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sqlite3

# insert_query = "INSERT INTO videos VALUES (?,?,?)"
# cursor.execute (insert_query, videos)
# cursor.executemany(insert_query, videos)

def find_videoname(catalogue_id):
    
    connection = sqlite3.connect('../VideoStream/instance/videos.sqlite')
    cursor = connection.cursor()    

    query = "SELECT path FROM videos WHERE catalogue_id=?"
    result = cursor.execute(query, (catalogue_id,))
    row = result.fetchone()
    
    return row

    connection.close
    

print find_videoname(0)        
