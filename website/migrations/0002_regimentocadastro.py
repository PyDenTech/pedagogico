# Generated by Django 5.1.1 on 2024-10-19 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegimentoCadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(choices=[('TÍTULO I', 'TÍTULO I - DAS DISPOSIÇÕES PRELIMINARES'), ('TÍTULO II', 'TÍTULO II - DAS FINALIDADES E OBJETIVOS DA EDUCAÇÃO BÁSICA'), ('TÍTULO III', 'TÍTULO III - DA ORGANIZAÇÃO DA INSTITUIÇÃO'), ('TÍTULO IV', 'TÍTULO IV - DOS PAIS OU RESPONSÁVEIS'), ('TÍTULO V', 'TÍTULO V - DAS DEMAIS ORGANIZAÇÃO DA INSTITUIÇÃO'), ('TÍTULO VI', 'TÍTULO VI - DA ADMINISTRAÇÃO PESSOAL'), ('TÍTULO VII', 'TÍTULO VII - DA ORGANIZAÇÃO DIDÁTICA - PEDAGÓGICA'), ('TÍTULO VIII', 'TÍTULO VIII - DO REGIME DE FUNCIONAMENTO'), ('TÍTULO IX', 'TÍTULO IX - DA VERIFICAÇÃO DO RENDIMENTO E AVALIAÇÃO'), ('TÍTULO X', 'TÍTULO X - DO REGIME DISCIPLINAR'), ('TÍTULO XI', 'TÍTULO XI - DAS DISPOSIÇÕES GERAIS E TRANSITÓRIAS')], max_length=255)),
                ('capitulo', models.CharField(max_length=255)),
                ('tipo_alteracao', models.CharField(choices=[('supressao', 'Supressão'), ('insercao', 'Inserção'), ('edicao', 'Alteração'), ('exclusao', 'Exclusão')], max_length=50)),
                ('justificativa', models.TextField()),
                ('nome_completo', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=14)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('cargo', models.CharField(blank=True, max_length=255, null=True)),
                ('lotacao', models.CharField(blank=True, max_length=255, null=True)),
                ('observacoes_adicionais', models.TextField(blank=True, null=True)),
                ('data_submissao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
