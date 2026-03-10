---
layout: post
title: "【FF14】特定の魚を狙う釣りにおけるスキル総合戦略の最適化モデル"
date: 2026-03-10 18:00:00 +0900
categories: [FF14, 釣り]
tags: []
math: true
mermaid: false
---

制限時間内に、どれだけ狙った魚を釣り上げられるか。

本記事では、その効率を数学的に最適化するためのアプローチとして、3段階に分かれたスキル戦略構築のプロセスを解説します。

## Step 1. 単一シナリオの評価
まずは「トレードリリースの対象」「撒き餌の有無」「ルアーの使用回数」「型確定の有無」といった状況パターンを完全に固定した、単一の「シナリオ」を作り、その基本性能を評価します。

例えば、「ルアーアクションを3回使って何も起こらなかった」あるいは「2回目で型が確定した」といった1つの状況がシナリオに該当します。

この段階での目的は、当該シナリオにおける **「ターゲット1匹を釣るための期待時間」** と **「秒間あたりの平均GP収支（消費と回復の差）」** という絶対的な指標を把握することです。



シナリオにおける各魚のヒット率を $p_i$、その魚が釣れるまでのサイクル時間を $t_i$ とすると、 **「平均サイクル時間 ($c$)」** は以下の計算で求められます。
$$ c = \sum (p_i \times t_i) $$

求められたサイクル時間 $c$ とターゲットのヒット率 $h$ を用いて、 **「ターゲット1匹を釣るための期待時間 ($E_{time}$)」** を算出します。
$$ E_{time} = \frac{c}{h} $$

さらに、そのシナリオにおける固定の各種スキル消費量 $GP_{cost}$ を $c$ で割ることで、 **「秒間あたりの平均GP消費量 ($GP_{sec}$)」** が算出されます。
$$ GP_{sec} = \frac{GP_{cost}}{c} $$
これらをもとに、秒間あたりの「GP回復力 ($GP_{rec}$)」との差分から **「秒間GP収支 ($GP_{net}$)」** を算出し、シナリオ単体の持続性（GPが黒字か赤字か）を評価します。
$$ GP_{net} = GP_{rec} - GP_{sec} $$
※ $GP_{rec}$（時間あたりのGP回復力）は、プレイヤーの自然回復（3秒ごとに8GP）と、アイテム「ハイコーディアル」使用（180秒ごとに400GP）による回復実績をそれぞれ秒間に均した数値（$8/3 + 400/180$ = 約4.88）を使用しています。

## Step 2. L戦略（ルアー戦略）の加重平均による実戦モデル化
実際の釣りにおいて「基本的にルアーを3回使うが、1,2回目で型が確定した場合は待機する」といった方針（L戦略）を定めた場合、その方針の中には事象の発生確率（例えば「2回目で型が確定する確率」など）に応じた複数の「固定シナリオ」が内包されています。

Step 1で行ったのは、そのうちの1つの固定シナリオが起きた場合の純粋な性能評価でした。Step 2では、それら複数の固定シナリオを各発生確率に基づいて加重平均し、ひとまとめにした「L戦略（ルアー戦略）」として包括的に評価します。

L戦略として評価することで、実戦運用時の「平均的なサイクル時間・GP収支・釣り上げ期待値」といった総合的な性能が算出できるようになります。

**[計算式: L戦略の加重平均]**
各分岐シナリオ $i$ に到達する確率を $P_i$、そのシナリオが持つ評価値（時間やGP収支など）を $V_i$ としたとき、L戦略全体の平均評価値 $V_{L}$ は加重平均により以下のように表されます。
$$ V_{L} = \sum (P_i \times V_i) $$

この段階でのゴールは、数あるL戦略の中から **「効率は低いがGPは着実に回復する（GP黒字）」** と、 **「効率は高いがGPを激しく消費する（GP赤字）」** という、性質の異なる2つの最適なL戦略の候補を見つけ出すことです。

## Step 3. 総合戦略（オプティマイザ）による最適解の導出
強力なL戦略の候補を抽出できたら、最後はそれらを制限時間内でどう配分するかという「総合戦略」の算出です。
「条件の制限時間（例: 7分）」と「実質的な使用可能GP（初期GP＋サリャクの恩寵等の回復見込み）」という2つのリソース上限を定めます。
先ほど導出した2戦略の能力を係数として当てはめ、 **「用意されたGPリソースを残さず使い切り、かつ制限時間内にぴったり収束する」** という条件で、最適となる実行配分（回数）を算出します。


赤字戦略Aと黒字戦略Bの実践回数をそれぞれ $n_A, n_B$ とし、それぞれの平均サイクル時間を $c_A, c_B$、1サイクルあたりの平均GP収支を $GP_{net,A}, GP_{net,B}$ とします。
制限時間を $T$、使用可能な総GPを $GP_{total}$ としたとき、以下の連立方程式が成り立ちます。

1. **時間制約**: $n_A \times c_A + n_B \times c_B = T$
2. **GP制約**: $n_A \times GP_{net,A} + n_B \times GP_{net,B} = -GP_{total}$

これを解き、最適な実行回数 $n_A, n_B$ を算出します。
行列式 $det = c_A \times GP_{net,B} - c_B \times GP_{net,A}$ としたとき、解は以下の通りです。
$$ n_A = \frac{T \times GP_{net,B} + c_B \times GP_{total}}{det} $$
$$ n_B = \frac{-c_A \times GP_{total} - T \times GP_{net,A}}{det} $$

これにより、「黒字戦略を◯回、赤字戦略を△回」という最適な配分が導き出せます。
この配分時の釣り上げ期待値が最も高くなる組み合わせが、該当条件下における「最適解」となります。

### 未知の確率への対応
なお、ターゲットヒット確率が不明な魚であっても、確率を「変数 ($p$)」のまま方程式に組み込んで計算比較することで、「どの総合戦略が最も優位か」という論理的な判断を下すことが可能です。

下記は、私が持っているデータを用いて実際に上記の計算を実装したツールで、リッチパースを狙う釣りにおける最適解を導出した例です。

赤字戦略「ルアー使用1回、撒き餌あり」を約19回と、黒字戦略「ルアー使用基本3回、型確定したら待機、撒き餌なし」を約4回が最適解となります。

 **[ツールでのシミュレーション結果（リッチパースの最適解）](https://ff-14-fisher-logic-engine.vercel.app/share.html?data=eyJ2ZXJzaW9uIjozLCJtb2RlIjoib3B0aW1pemVyIiwic3BvdCI6Iua6gOOBoeOBn%2BeOhOmWoiIsIndlYXRoZXIiOiLmm4fjgorpm6gxNi0xOCIsImJhaXQiOiLjgrTjg7zjgrnjg4jjg4vjg4Pjg5Hjg7wiLCJ0YXJnZXQiOiLjg6rjg4Pjg4Hjg5Hjg7zjgrkiLCJpc0NhdGNoQWxsIjpmYWxzZSwiaXNWYXJpYWJsZU1vZGUiOmZhbHNlLCJzbGFwRmlzaCI6IumHkeOBrumJviIsImlzQ2h1bSI6dHJ1ZSwibHVyZVR5cGUiOiLjgqLjg7Pjg5Pjgrfjg6Pjgrnjg6vjgqLjg7wiLCJsdXJlQ291bnQiOiIzIiwibHVyZVN0ZXAxIjoibm9uZSIsImx1cmVTdGVwMiI6Im5vbmUiLCJsdXJlU3RlcDMiOiJub25lIiwic3RyYXRBIjp7Imx1cmVUeXBlIjoi44Ki44Oz44OT44K344Oj44K544Or44Ki44O8IiwicXVpdCI6Im5vIiwicHJlc2V0IjoiYjNfZ3Vhcl9zdG9wIiwic2xhcCI6IumHkeOBrumJviIsImNodW0iOiJ5ZXMifSwic3RyYXRCIjp7Imx1cmVUeXBlIjoi44Ki44Oz44OT44K344Oj44K544Or44Ki44O8IiwicXVpdCI6Im5vIiwicHJlc2V0IjoiZml4ZWRfbDEiLCJzbGFwIjoi6YeR44Gu6Ym%2BIiwiY2h1bSI6InllcyJ9LCJvcHQiOnsidGltZSI6IjM1MCIsImdwIjoiMTAwMCIsInNhbGphayI6IjAiLCJzZXRBIjp7Imx1cmUiOiLjgqLjg7Pjg5Pjgrfjg6Pjgrnjg6vjgqLjg7wiLCJwcmVzZXQiOiJmaXhlZF9sMSIsInNsYXAiOiLph5Hjga7pib4iLCJjaHVtIjoieWVzIn0sInNldEIiOnsibHVyZSI6IuOCouODs%2BODk%2BOCt%2BODo%2BOCueODq%2BOCouODvCIsInByZXNldCI6ImIzX2d1YXJfc3RvcCIsInNsYXAiOiLph5Hjga7pib4iLCJjaHVtIjoibm8ifX19)**


## おわりに
以上の計算を精密に行い、最適な総合戦略を見つけ出すためには、各釣り場での「魚の基本ヒット率」や「型確定発生率」といった正確なデータが必要不可欠です。
こうしたデータ収集は非常に重要になります。今後も多くの漁師の皆さんと協力してデータを提供し合い、より精度の高い最適解を作り上げていければと思います。