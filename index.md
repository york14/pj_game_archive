---
layout: page
title: Home
---

<div id="post-list" class="flex-grow-1 px-xl-1">
  {% for post in site.posts %}
  <article class="card-wrapper card">
    <a href="{{ post.url | relative_url }}" class="post-preview row g-0 flex-md-row-reverse" style="text-decoration: none;">
      <div class="col-md-12">
        <div class="card-body d-flex flex-column">
          <h1 class="card-title my-2 mt-md-0">{{ post.title }}</h1>
          <div class="card-text content mt-0 mb-3" style="color: var(--text-muted-color);">
            <p>記事を読む &rarr;</p>
          </div>
          <div class="post-meta flex-grow-1 d-flex align-items-end text-muted">
            <div class="me-auto">
              <i class="far fa-calendar fa-fw me-1"></i>
              <time>{{ post.date | date: "%Y-%m-%d" }}</time>
            </div>
            {% if post.categories.size > 0 %}
            <i class="far fa-folder fa-fw me-1"></i>
            <span class="categories">
              {{ post.categories | join: ', ' }}
            </span>
            {% endif %}
          </div>
        </div>
      </div>
    </a>
  </article>
  {% endfor %}
</div>
