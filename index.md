---
layout: page
title: Home
---

## 投稿記事一覧 (Debug)

<ul>
{% for post in site.posts %}
  <li>
    <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br>
    <small>{{ post.date | date: "%Y-%m-%d" }}</small>
  </li>
{% endfor %}
</ul>
