# Generated by Django 2.1.4 on 2018-12-10 16:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.CharField(blank=True, max_length=250)),
                ('summary_image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Image')),
                ('summary_image_size', models.CharField(default='big', help_text="Choose 'LEAVE' if image size should not be changed.", max_length=20)),
                ('summary_image_alt', models.CharField(blank=True, help_text='Description of image for assistive technology.', max_length=200)),
                ('summary_text', models.TextField(blank=True)),
                ('byline', models.CharField(blank=True, help_text='If this is not blank it overrides the value of the author fields', max_length=200, verbose_name='customised byline')),
                ('byline_style', models.CharField(choices=[('ST', 'Standard'), ('TP', 'Text By [First Author] Photos By [Second Author]')], default='ST', max_length=2)),
                ('primary_image', filebrowser.fields.FileBrowseField(blank=True, max_length=200)),
                ('primary_image_size', models.CharField(default='extra_large', help_text="Choose 'LEAVE' if image size should not be changed.", max_length=20)),
                ('primary_image_alt', models.CharField(blank=True, help_text='Description of image for assistive technology.', max_length=200)),
                ('external_primary_image', models.CharField(blank=True, help_text='Use this instead of primary. But note that if primary image has a value, it overrides this.', max_length=500, verbose_name='alternative URL')),
                ('primary_image_caption', models.CharField(blank=True, max_length=600)),
                ('body', models.TextField(blank=True)),
                ('use_editor', models.BooleanField(default=True)),
                ('published', models.DateTimeField(blank=True, null=True, verbose_name='publish time')),
                ('recommended', models.BooleanField(default=True)),
                ('copyright', models.TextField(blank=True, default='<p>&copy; 2018 GroundUp.<a rel="license"   href="http://creativecommons.org/licenses/by-nd/4.0/">    <svg viewBox="0 0 100 100"         class="icon icon-creative-commons">        <use xlink:href="#icon-creative-commons">        </use>    </svg></a><br />This article is licensed under a <a rel="license"   href="http://creativecommons.org/licenses/by-nd/4.0/">Creative Commons Attribution-NoDerivatives 4.0 International License</a>.</p><p>You may republish this article, so long as you credit the authors and GroundUp, and do not change the text. Please include a link back to the original article.</p>')),
                ('template', models.CharField(choices=[('newsroom/article_detail.html', 'Standard')], default='newsroom/article_detail.html', max_length=200)),
                ('summary_template', models.CharField(choices=[('newsroom/article_summary.html', 'Standard'), ('newsroom/photo_summary.html', 'Great Photo'), ('newsroom/text_summary.html', 'Text only')], default='newsroom/article_summary.html', max_length=200)),
                ('include_in_rss', models.BooleanField(default=True)),
                ('letters_on', models.BooleanField(default=True)),
                ('comments_on', models.BooleanField(default=False)),
                ('collapse_comments', models.BooleanField(default=True)),
                ('exclude_from_list_views', models.BooleanField(default=False)),
                ('suppress_ads', models.BooleanField(default=False, help_text='Only suppresses ads that are external to article. You can still create ads in article.')),
                ('promote_article', models.BooleanField(default=True)),
                ('encourage_republish', models.BooleanField(default=True)),
                ('activate_slideshow', models.BooleanField(default=False)),
                ('additional_head_scripts', models.TextField(blank=True)),
                ('additional_body_scripts', models.TextField(blank=True, help_text='Include things like additional javascript that should come at bottom of article')),
                ('undistracted_layout', models.BooleanField(default=False)),
                ('disqus_id', models.CharField(blank=True, max_length=20)),
                ('stickiness', models.IntegerField(default=0, help_text='The higher the value, the stickier the article.')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('facebook_wait_time', models.PositiveIntegerField(default=0, help_text='Minimum number of minutes after publication till post.')),
                ('facebook_image', filebrowser.fields.FileBrowseField(blank=True, help_text='Leave blank to use primary image.', max_length=200, verbose_name='image')),
                ('facebook_image_caption', models.CharField(blank=True, help_text='Leave blank to use primary image caption.', max_length=200, verbose_name='caption')),
                ('facebook_description', models.CharField(blank=True, help_text='Leave blank to use same text as summary.', max_length=200)),
                ('facebook_message', models.TextField(blank=True, help_text='Longer status update that appears above the image in Facebook. ', verbose_name='message')),
                ('facebook_send_status', models.CharField(choices=[('scheduled', 'Scheduled'), ('sent', 'Sent'), ('failed', 'Failed'), ('paused', 'Paused')], default='paused', max_length=20, verbose_name='sent status')),
                ('last_tweeted', models.DateTimeField(default=datetime.datetime(1999, 12, 31, 22, 0, tzinfo=utc))),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=0)),
                ('notified_authors', models.BooleanField(default=False)),
                ('author_payment', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('override_commissions_system', models.CharField(choices=[('NO', 'No'), ('PROCESS', 'Process commissions for this article'), ('NOPROCESS', "Don't process commissions for this article")], default='NO', max_length=20)),
                ('commissions_processed', models.BooleanField(default=False)),
                ('cached_byline', models.CharField(blank=True, max_length=500)),
                ('cached_byline_no_links', models.CharField(blank=True, max_length=400, verbose_name='Byline')),
                ('cached_primary_image', models.URLField(blank=True, max_length=500)),
                ('cached_summary_image', models.URLField(blank=True, max_length=500)),
                ('cached_summary_text', models.TextField(blank=True)),
                ('cached_summary_text_no_html', models.TextField(blank=True)),
                ('cached_small_image', models.URLField(blank=True, max_length=500)),
            ],
            options={
                'ordering': ['-stickiness', '-published'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_names', models.CharField(blank=True, max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('freelancer', models.BooleanField(default=False)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('title', models.CharField(blank=True, max_length=20)),
                ('telephone', models.CharField(blank=True, max_length=200)),
                ('cell', models.CharField(blank=True, max_length=200)),
                ('identification', models.CharField(blank=True, help_text='SA ID, passport or some form of official identification', max_length=20)),
                ('dob', models.DateField(blank=True, help_text='Please fill this in. Required by SARS.', null=True, verbose_name='date of birth')),
                ('address', models.TextField(blank=True, help_text='Please fill this in. Required by SARS.')),
                ('bank_name', models.CharField(blank=True, max_length=20)),
                ('bank_account_number', models.CharField(blank=True, max_length=20)),
                ('bank_account_type', models.CharField(default='CURRENT', max_length=20)),
                ('bank_branch_name', models.CharField(blank=True, help_text='Unnecessary for Capitec, FNB, Standard, Nedbank and Absa', max_length=20)),
                ('bank_branch_code', models.CharField(blank=True, help_text='Unnecessary for Capitec, FNB, Standard, Nedbank and Absa', max_length=20)),
                ('swift_code', models.CharField(blank=True, help_text='Only relevant for banks outside SA', max_length=12)),
                ('iban', models.CharField(blank=True, help_text='Only relevant for banks outside SA', max_length=34)),
                ('tax_no', models.CharField(blank=True, help_text='Necessary for SARS.', max_length=50)),
                ('tax_percent', models.DecimalField(decimal_places=0, default=25, help_text='Unless you have a tax directive we have to deduct 25% PAYE for SARS.', max_digits=2, verbose_name='tax %')),
                ('vat', models.DecimalField(decimal_places=0, default=0, help_text='If you are VAT regisered set this to 14 else leave at 0', max_digits=2, verbose_name='vat %')),
                ('email_is_private', models.BooleanField(default=True)),
                ('photo', filebrowser.fields.FileBrowseField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('twitter', models.CharField(blank=True, max_length=200)),
                ('facebook', models.CharField(blank=True, max_length=200)),
                ('googleplus', models.CharField(blank=True, max_length=200)),
                ('password_changed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['last_name', 'first_names'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MostPopular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_list', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'most popular',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('introduction', models.TextField(blank=True, help_text='Use unfiltered HTML. If this is not blank, the default template does not render any other fields before the article list.')),
                ('icon', filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Image')),
                ('template', models.CharField(default='newsroom/topic_detail.html', max_length=200)),
                ('newest_first', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UserEdit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed', models.BooleanField(default=False)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsroom.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['article__published', 'edit_time'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='author_01',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_01', to='newsroom.Author', verbose_name='first author'),
        ),
        migrations.AddField(
            model_name='article',
            name='author_02',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_02', to='newsroom.Author', verbose_name='second author'),
        ),
        migrations.AddField(
            model_name='article',
            name='author_03',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_03', to='newsroom.Author', verbose_name='third author'),
        ),
        migrations.AddField(
            model_name='article',
            name='author_04',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_04', to='newsroom.Author', verbose_name='fourth author'),
        ),
        migrations.AddField(
            model_name='article',
            name='author_05',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_05', to='newsroom.Author', verbose_name='fifth author'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='newsroom.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='main_topic',
            field=models.ForeignKey(blank=True, help_text="Used for generating'See also' list of articles.", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main', to='newsroom.Topic'),
        ),
        migrations.AddField(
            model_name='article',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newsroom.Region'),
        ),
        migrations.AddField(
            model_name='article',
            name='topics',
            field=models.ManyToManyField(blank=True, to='newsroom.Topic'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='useredit',
            unique_together={('article', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='author',
            unique_together={('first_names', 'last_name')},
        ),
    ]
