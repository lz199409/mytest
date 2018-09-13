# -*- coding: utf-8 -*-

from odoo import models, fields, api


class openacademy(models.Model):
    _name = 'openacademy.openacademy'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()


class Course(models.Model):
    _name = "openacademy.course"

    name = fields.Char(string=u"科目", required=True)
    description = fields.Text(string=u"描述")
    # 设置Many2one关系，将课程表和res.user这张表进行关联
    # res.user这张表是系统中保留用户登录信息的表
    # 多个课程可以对应一个用户，一个用户也可以对应多个课程
    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null', string="负责人", index=True)
    session_ids = fields.One2many('openacademy.session', "course_id", string="Sessions")

class Session(models.Model):
    _name = "openacademy.session"

    name = fields.Many2one("student_info", required=True, string=u"学生姓名", ondelet="cascade")
    start_date = fields.Date(string=u"开始时间")
    duration = fields.Float(string=u"学时", digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="座位数")
    # 对课时设置一个指导人
    instructor_id = fields.Many2one('res.partner', string=u"指导人")
    # 课时关联到课程
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string=u"课程",
                                required=True)
    attende_ids = fields.Many2many("student_info", string="Attendees")

class SessionExtension(models.Model):
    _inherit = 'openacademy.session'

    description = fields.Text(string="描述信息")

class SessionCopy(models.Model):
    _name = 'openacademy.session.copy'
    _inherit = 'openacademy.session'

    copy = fields.Text(string="Copy")


class Student(models.Model):
    _name = "student_info"
    _description = u"学生信息"

    name = fields.Char(string=u"姓名", required=True)
    age = fields.Integer(string=u"年龄")
    sex = fields.Selection([(1, "男"), (2, "女")], string=u"性别", default=1, help="请选择性别")
    score = fields.Float(string=u"成绩", required=True, default=0.0, digits=(10, 2))
    date_time = fields.Datetime(string=u"创建时间", required=True, readonly=True, default=fields.Datetime.now)
    std_cor_id = fields.Many2many("openacademy.course", string=u"选课信息")

class Child0(models.Model):
    _name = 'delegation.child0'

    field_0 = fields.Integer()

class Child1(models.Model):
    _name = 'delegation.child1'

    field_1 = fields.Integer()

class Delegating(models.Model):
    _name = 'delegation.parent'

    _inherits = {
        'delegation.child0': ''
    }



