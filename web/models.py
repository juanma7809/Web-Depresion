# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Entrevista(models.Model):
    id_entrevista = models.IntegerField(blank=True, null=True)
    entrevistador = models.CharField(max_length=255, blank=True, null=True)
    fecha_entrevista = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entrevista'


class Formulario(models.Model):
    id_formulario = models.IntegerField(blank=True, null=True)
    nombre_formulario = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formulario'


class Paciente(models.Model):
    id_paciente = models.IntegerField(blank=True, null=True)
    id_rol = models.IntegerField(blank=True, null=True)
    nombres = models.CharField(max_length=255, blank=True, null=True)
    apellidos = models.CharField(max_length=255, blank=True, null=True)
    correo = models.CharField(max_length=255, blank=True, null=True)
    contrasena = models.CharField(max_length=255, blank=True, null=True)
    cedula = models.CharField(max_length=255, blank=True, null=True)
    fecha_nacimiento = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'


class PacienteAudio(models.Model):
    id_paciente_audio = models.IntegerField(blank=True, null=True)
    id_paciente = models.IntegerField(blank=True, null=True)
    id_audio = models.IntegerField(blank=True, null=True)
    id_entrevista = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente_audio'


class PacienteFormulario(models.Model):
    id_paciente_formulario = models.IntegerField(blank=True, null=True)
    id_paciente = models.IntegerField(blank=True, null=True)
    id_formulario = models.IntegerField(blank=True, null=True)
    id_entrevista = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente_formulario'


class PacienteVideo(models.Model):
    id_paciente_video = models.IntegerField(blank=True, null=True)
    id_paciente = models.IntegerField(blank=True, null=True)
    id_video = models.IntegerField(blank=True, null=True)
    id_entrevista = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente_video'


class Permiso(models.Model):
    id_permiso = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permiso'


class Pregunta(models.Model):
    id_pregunta = models.IntegerField(blank=True, null=True)
    pregunta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pregunta'


class PreguntasFormualrio(models.Model):
    id_formulario_preguntas = models.IntegerField(blank=True, null=True)
    id_formulario = models.IntegerField(blank=True, null=True)
    id_pregunta = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preguntas_formualrio'


class RespuestaDepresion(models.Model):
    id_respuesta = models.IntegerField(blank=True, null=True)
    id_paciente = models.IntegerField(blank=True, null=True)
    id_video_respuesta = models.IntegerField(blank=True, null=True)
    id_audio_respuesta = models.IntegerField(blank=True, null=True)
    nivel_depresion = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_diagnostico = models.CharField(max_length=255, blank=True, null=True)
    id_entrevista = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respuesta_depresion'


class Rol(models.Model):
    id_rol = models.IntegerField(blank=True, null=True)
    nombre_rol = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class RolPermisos(models.Model):
    id_rol_permisos = models.IntegerField(blank=True, null=True)
    id_rol = models.IntegerField(blank=True, null=True)
    id_permiso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol_permisos'


class Usuario(models.Model):
    id_usuario = models.IntegerField(blank=True, null=True)
    id_rol = models.IntegerField(blank=True, null=True)
    nombres = models.CharField(max_length=255, blank=True, null=True)
    apellidos = models.CharField(max_length=255, blank=True, null=True)
    correo = models.CharField(max_length=255, blank=True, null=True)
    contrasena = models.CharField(max_length=255, blank=True, null=True)
    cedula = models.CharField(max_length=255, blank=True, null=True)
    fecha_nacimiento = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
