---
layout: default
title: "AKE: ダメージ計算式の全体像"
---

# ダメージ計算式の全体像

## 概要
Arknights: Endfield のダメージ計算は**15種の独立した倍率項の乗算**で構成される。各項が独立しているため、1つの項を伸ばすことの効果が直感的に把握しやすい。

## 計算式

```
Final Damage = Final ATK × Base Multiplier × Π(各倍率項)
```

### ATK の算出
```
ATK = ((Operator ATK + Weapon ATK) × (1 + ATK+%) + Fixed Bonus + Special Bonus) × Attribute Bonus
Attribute Bonus = 1 + 0.005 × Main Attribute + 0.002 × Sub Attribute
```

### 15種の倍率項

| # | 項目 | 説明 |
|---|---|---|
| 1 | ATK+% | 攻撃力の割合増加 |
| 2 | Base Multiplier | スキル倍率 |
| 3 | DMG Bonus | 与ダメージ増加 |
| 4 | Critical DMG | クリティカルダメージ |
| 5 | Amplification | 増幅 |
| 6 | Stagger Bonus | よろめきボーナス |
| 7 | Finisher | 仕留め |
| 8 | Link Bonus | 連携ボーナス |
| 9 | Weaken | 脆弱 |
| 10 | Susceptibility | 被弾感度 |
| 11 | Increased DMG Taken | 被ダメ増加 |
| 12 | DMG Reduction | ダメージ軽減（減算） |
| 13 | Protection | 被ダメ減少（減算） |
| 14 | DEF Multiplier | 防御力計算（100 / (DEF + 100)） |
| 15 | Resistance | 属性耐性 |

## 考察
- 項1（ATK+%）はATK計算に組み込まれるため、最終乗算には含めない
- 各項は独立しているため、**最も低い項を伸ばすのが効率的**（乗算のバランス原理）
- DEF Multiplierは敵の防御力依存のため、プレイヤー側で操作しにくい

---
*最終更新: 2026-03-04*
