from github import Github

# 你的 GitHub 用户名和密码（或访问令牌）
username = 'your_username'
password = 'your_password'

# 仓库名称和文件路径
repository_name = 'your_repository'
file_path = 'pathtoyourfile.txt'

# 创建 GitHub 对象
g = Github(username, password)

# 获取指定的仓库
repo = g.get_user().get_repo(repository_name)

# 读取文件内容
with open(file_path, 'r') as file
    content = file.read()

# 提交文件到仓库
repo.create_file(file_path, commit message, content)
