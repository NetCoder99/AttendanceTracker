import sqlite3

from sqlite.sqlite_procs import DictFactory


# ------------------------------------------------------------------
def GetSqliteStudents(db_path: str):
    dbObj = sqlite3.connect(db_path)
    dbObj.row_factory = DictFactory
    cursor = dbObj.cursor()
    cursor.execute(GetStudentRecordsStmt())
    rows = cursor.fetchall()
    dbObj.close()
    return rows


def GetStudentRecordsStmt():
    return '''
        SELECT badgeNumber,
           firstName,
           lastName,
           namePrefix,
           email,
           address,
           address2,
           city,
           country,
           state,
           zip,
           birthDate,
           phoneHome,
           phoneMobile,
           status,
           memberSince,
           gender,
           currentRank,
           ethnicity,
           studentImageBytes,
           studentImagePath,
           studentImageBase64,
           middleName,
           studentImageName,
           studentImageType,
           currentRankName
      FROM students;
    '''