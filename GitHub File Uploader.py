from github import Github

# ��� GitHub �û��������루��������ƣ�
username = 'your_username'
password = 'your_password'

# �ֿ����ƺ��ļ�·��
repository_name = 'your_repository'
file_path = 'pathtoyourfile.txt'

# ���� GitHub ����
g = Github(username, password)

# ��ȡָ���Ĳֿ�
repo = g.get_user().get_repo(repository_name)

# ��ȡ�ļ�����
with open(file_path, 'r') as file
    content = file.read()

# �ύ�ļ����ֿ�
repo.create_file(file_path, commit message, content)
