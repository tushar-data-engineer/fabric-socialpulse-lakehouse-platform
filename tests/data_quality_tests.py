def test_no_null_userid(df):
    assert df.filter(df.userId.isNull()).count() == 0
