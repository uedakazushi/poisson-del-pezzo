# Poisson structures on del Pezzo manifolds

**次数1・2を中心に、del Pezzo manifold の Poisson 構造・葉の幾何・量子化を研究する。**

2026-11-20（JST） / v1.0

再開時は [研究方針](00_research_plan.md) を最初に読み、[研究ノート](research/research_notes.md)、[現行論文](papers/dp12_poisson.tex) の順に進む。現行ソース・必要な計算・参照文献をこのリポジトリの `main` で管理する。

## 現在の中心結果

$X$ を滑らかな複素 $n$ 次元 del Pezzo manifold、$n\geq2$、$-K_X=(n-1)H$、$d=H^n\in\{1,2\}$ とする。固定した $X$ 上で、Schouten 括弧の二次写像 $\pi\mapsto\frac12[\pi,\pi]$ の零スキームを $\operatorname{Pois}_{\mathrm{sch}}(X)$ と定義する。

| 次数 | 大域二重ベクトル空間の次元 | Poisson スキーム | 非零構造の一般階数 |
| --- | --- | --- | --- |
| 1 | $n$ | $\mathbb A^n$ | 2 |
| 2 | $\binom{n+1}{2}$ | $\operatorname{Gr}(2,n+1)$ の Plücker affine cone | 2 |

**次数2では、Jacobi イデアルと Plücker イデアルの一致を証明している。** 被約化した点集合だけでなく、非被約な基底上の係数族にも適用できる。零 Poisson 構造の一次変形は全ての二重ベクトルを許すが、二次へ持ち上がるには外積二乗が零でなければならない。

非零構造のスカラーによる射影化は、内在的に $\operatorname{Gr}(n-1,H^0(X,H))$ となる。標準重み付き ambient stack への一意な延長と、定義式を Casimir とする cone 上の一意な代表を与える。一般の Poisson 構造の一般の葉の閉包は同じ次数の滑らかな del Pezzo 曲面となり、各構造に中心的超曲面による次数付き形式量子化が存在する。

これらの証明は現行論文に記載し、分類・スキームの証明と形式量子化の適用を今回点検した。**新規性は未確定。** 曲面の場合と三次元の集合論的分類は既知であり、形式量子化は Kontsevich、曲面の potential は Etingof–Ginzburg の定理を入力にする。文献との区別は [文献メモ](research/literature_notes.md)、実行した確認の範囲は [検証・再現手順](docs/reproduction.md) を参照する。

## 原稿と研究資産

| ファイル | 役割 |
| --- | --- |
| [00_research_plan.md](00_research_plan.md) | 目標、主張の状態、次に着手する課題、恒常的な研究原則 |
| [papers/dp12_poisson.tex](papers/dp12_poisson.tex) | 日本語 LuaLaTeX の公表用研究原稿。分類・スキーム・葉・曲面退化・形式量子化 |
| [research/research_notes.md](research/research_notes.md) | 記法、証明の依存、相対化の着手方法、未解決の障害 |
| [research/dp4_comparison.md](research/dp4_comparison.md) | 次数4との比較、階数4の例、lift の非一意性、具体的量子化模型 |
| [research/literature_notes.md](research/literature_notes.md)・[references.bib](references.bib) | 一次資料の参照箇所と未確認事項 |
| [computations/verify_jacobi.py](computations/verify_jacobi.py) | Casimir 条件・Jacobi 公式・Plücker 係数回収の厳密検算 |
| [docs/reproduction.md](docs/reproduction.md) | 組版、検算、確認範囲 |

論文は章のまとまりに応じた三つのソースを `papers/sections/` から読み込む。一つの論文を構成するための分割であり、次数ごとの別論文ではない。生成 PDF と組版の中間ファイルは追跡しない。

```sh
python3 -m pip install -r requirements.txt
make verify
make pdf
```

`make pdf` は LuaLaTeX・LuaTeX-ja・BibTeX・latexmk と Noto CJK フォントを使い、`build/dp12_poisson.pdf` を生成する。

## 次の課題

1. **相対 Jacobi スキーム。** 滑らかな定義方程式の族上で Euler–Koszul 計算と係数回収を行い、基底変換と両立する記述を与える。
2. **内在的な同変性。** 座標・定義式の変更に伴う twist を求め、スカラー商・自己同型商・動く多様体のモジュライを区別する。
3. **公表前の文献比較。** 任意次元の分類、ambient lift、スキーム論的強化について既知性をそれぞれ確認する。

非形式的な量子化の代数化、全特殊化での AS 正則性、全ての非可換圏変形の網羅性は未解決の別課題である。

## 関連リポジトリとの分担

- **次数1・2と共通の比較**：本リポジトリ。
- **次数3の一般次元 cubic hypersurface**：[nc-cubic](https://github.com/uedakazushi/nc-cubic)。既存の分類・量子化原稿を正本とする。
- **次数4の二次完全交叉**：[poisson-22ci](https://github.com/uedakazushi/poisson-22ci) の支持成長・剛性と、[nc-22ci](https://github.com/uedakazushi/nc-22ci) の一般構造・五次元解析を参照する。本リポジトリの比較ノートは、それらの詳細分類の代わりではない。
- **次数1の非可換圏の認識・モジュライ**：[nc-dp1-moduli](https://github.com/uedakazushi/nc-dp1-moduli)。Poisson 構造から量子化を作る問題と、既存の圏から ambient を認識する問題を区別する。
- **研究全体の入口**：[research-hub](https://github.com/uedakazushi/research-hub)。
