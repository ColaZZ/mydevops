import pexpect


def login_ssh_passwd(port="", user="", host="", passwd=""):
    """
    用于实现pexepect实现ssh的自动化用户密码登录
    ssh -p user@host
    :param host:    访问的host
    :param port:    访问接口port
    :param user:    访问的用户
    :param password: 访问用户的密码
    :return:    print打印出是否访问成功
    """
    if host and port and user and passwd:
        ssh = pexpect.spawn('ssh -p %s %s@%s' % (port, user, host))
        i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=5)
        if i == 0:
            ssh.sendline(passwd)
        elif i == 1:
            ssh.sendline('yes\n')
            ssh.expect('password: ')
            ssh.sendline(passwd)
        index = ssh.expect(['#', pexpect.EOF, pexpect.TIMEOUT])

        if index == 0:
            print('logging as root')
            ssh.interact()
        elif index == 1:
            print('logging process exit')
        elif index == 2:
            print('logging timeout exit')

    else:
        print('Parameter error')


def login_ssh_key(keyfile="", user="", host="", port=""):
    """
    用于实现pexpect实现ssh的自动化秘钥登录
    ssh -i key -p port user@host
    :param keyfile:
    :param user:
    :param host:
    :param port:
    :return:
    """

    if keyfile and user and host and port:
        ssh = pexpect.spawn('ssh -i %s -p %s %s@%s' % (keyfile, port, user, host))
        i = ssh.expect([pexpect.TIMEOUT, 'continue connecting (yser/no)?'], timeout=5)
        if i == 1:
            ssh.sendline('yes\n')
            index = ssh.expect(["#", pexpect.EOF, pexpect.TIMEOUT])
        else:
            index = ssh.expect(["#", pexpect.EOF, pexpect.TIMEOUT])

        if index == 0:
            print('logging as root')
        elif index == 1:
            print('logging process exit')
        elif index == 2:
            print('logging timeout exit')
    else:
        print('Parameter error')


def main():
    """
        主函数：实现两种方式分别的登录
    :return:
    """
    # login_ssh_passwd(port='22',user='root',host='192.168.1.101',passwd='imooccs')
    login_ssh_key(keyfile="/tmp/id_rsa", port='22', user='root', host='192.168.1.101')


if __name__ == "__main__":
    main()
