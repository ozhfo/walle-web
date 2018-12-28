# -*- coding: utf-8 -*-
"""
    walle-web

    :copyright: © 2015-2019 walle-web.io
    :created time: 2018-12-23 20:18:11
    :author: wushuiyong@walle-web.io
"""
from . import Notice
from walle.service import emails


class Email(Notice):

    def deploy_task(self, project_info, notice_info):
        '''
        上线单新建, 上线完成, 上线失败

        @param hook:
        @param notice_info:
            'title',
            'username',
            'project_name',
            'task_name',
            'branch',
            'commit',
            'is_branch',
        @return:
        '''
        message = u""" %s %s 
                <br><br> <strong>项目</strong>：%s
                <br><br> <strong>任务</strong>：%s
                <br><br> <strong>分支</strong>：%s
                <br><br> <strong>版本</strong>：%s
                <br><br><br><img src='http://walle-web.io/dingding.jpg'> """ % (
                notice_info['username'], notice_info['title'], notice_info['project_name'], notice_info['task_name'],
                notice_info['branch'], notice_info['commit'])
        emails.send_email(project_info['notice_hook'], notice_info['title'], message, '')
