import rhodecode

repo = rhodecode.get_repository(url="http://localhost:12000/svn/repos/xyzzy")
repo.update(author="admin", message="My first update")
