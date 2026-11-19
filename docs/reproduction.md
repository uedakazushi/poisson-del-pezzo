# 再現手順と検証範囲

2026-11-20（JST） / v1.2

## 1. 正本と必要なファイル

正本は GitHub `main` のソースである。[主原稿](../poisson-del-pezzo.tex) は `papers/sections/` の七つの TeX と [references.bib](../references.bib) を読み込む。[研究方針](../00_research_plan.md) と [研究ノート](../research/research_notes.md) から再開できる。旧原稿や過去の会話を必要としない。

生成 PDF、SyncTeX、組版の中間ファイル、検算の標準出力は `build/` に置き、Git の追跡対象から除外する。再現コードを残すので、大量の生成出力は収録しない。

## 2. 数学的な点検

本段階で点検した中心部分は次の通り。

- 固定対象の weighted Euler 列、Casimir 表示、偏微分の Koszul 完全性、Jacobi イデアルの線型回収を、族の定理の入力として確認した。
- 普遍切断による有限自由複体の分裂と、非被約基底を含む任意基底変換を証明・独立点検した。
- 相対 Euler 単射と勾配係数行列の局所左逆による、相対 Jacobi イデアルと Plücker イデアルの一致を点検した。$p_*\wedge^3T$ の局所自由性を仮定していない。
- 相対切断環からの正規形の構成、標準形間の全座標変更、正しい Poisson parameter の変換因子を確認した。
- 相対 Picard 層と基本偏極類の一意性を確認し、大域的な線束の選択とは区別した。平方零拡大での形式的 étale 性には、族の切断を étale 局所的に選んで線束を持ち上げる議論を記した。
- 線束のスカラー自己同型の除去、商スタックの代数性、$H^0(T_X)=0$ による DM 性、忘却射の affine 性・平坦性・有限表示性を点検した。
- 内在的な線束の twist、射影 Grassmann 族の降下、スタックの次元と非滑らかな点の集合、同時変形の二次障害を確認した。

これは人が読める証明の論理的点検であり、Lean 等による形式化ではない。引用した一般定理の全証明を独立に再証明したものでもない。新規性の包括的確認、coarse space の具体的構成、コンパクト化、相対量子化の降下は未完了である。

葉の幾何・曲面退化・形式量子化・条件付き AS 拡大の有効な本文は保持した。量子化の全証明および [次数4比較ノート](../research/dp4_comparison.md) の全面的な再監査は本段階の点検範囲に含めていない。本文に証明があることと、今回独立に点検したことを区別する。

- 零切断の blow-up が相対 Grassmann 上の tautological line の全空間になる同変な構成と、Gorenstein terminal の discrepancy を `sec:singularities` に記述した。射影正規性・ACM 性・MMP の一般結果は文献を入力とし、別途形式的証明は行っていない。

## 3. 厳密な記号検算

Python 3 と SymPy を用いる。確認環境は **Python 3.12.14 / SymPy 1.14.0**。

```sh
python3 -m pip install -r requirements.txt
make verify
```

`make verify` は三つのスクリプトを順に実行する。浮動小数点近似やランダム標本を用いない。

| スクリプト・対象 | 実行範囲 | 確認内容 | 結果 |
| --- | --- | --- | --- |
| `verify_jacobi.py`、次数1 | $n=2,3,5$ | Casimir 条件、Jacobi 恒等式49組 | 成功 |
| 同、次数2 | $n=2,3,4,5$ | Casimir 条件、Jacobiator69組、Plücker 係数回収 | 成功 |
| 同、零点の変形 | 四つの独立な $x$ 方向 | 階数4方向が一次では許され二次で障害を持つ | 成功 |
| `verify_families.py`、次数1の同変性 | $n=2$、方程式と $D$ の係数は全て独立記号 | 指定した非対角行列による bivector の直接 pushforward と $t^{-1}AD$ の一致 | 成功 |
| 同、次数2の同変性 | $n=3$、方程式と $P$ の係数は全て独立記号 | 直接 pushforward と $b^{-1}(\wedge^2A)P$ の一致、Plücker 関係の変換 | 成功 |
| 同、involution と中央スカラー | 上の両模型 | $z\mapsto-z$ の符号反転、重み付きスカラーの自明な作用 | 成功 |
| 同、動く方程式と二次障害 | 任意の一次勾配変化、一般の $Q,R$、$\varepsilon^3=0$ | Jacobiator の二次項に方程式の変化と $R$ が現れない | 成功 |

| `verify_cone.py`、次元・方程式数 | $2\leq n\leq19$ | lci の必要条件、discrepancy の数式の整数チェック | 成功 |

Jacobi のスクリプトは独立な勾配と対称 Hessian を使う。族のスクリプトは具体的な非対角座標変更について二重ベクトルの pushforward を直接計算する。これは式の符号・重み・二次障害の検証であり、任意次元の定理、基底変換、同型の網羅性、スタックの表現可能性を計算だけで証明するものではない。一般の証明は本文に置く。

## 4. LuaLaTeX 組版

TeX Live の LuaTeX、LuaTeX-ja、BibTeX、latexmk と Noto Serif CJK JP / Noto Sans CJK JP を用意する。主なパッケージは `fix-cm`, `amsmath`, `amssymb`, `amsthm`, `mathtools`, `bm`, `geometry`, `booktabs`, `longtable`, `array`, `hyperref`, `luatexja-fontspec`。

ルートから次のいずれかを実行する。

```sh
make pdf
latexmk
```

主ファイルは `poisson-del-pezzo.tex`。出力は `build/poisson-del-pezzo.pdf` と `build/poisson-del-pezzo.synctex.gz`。`.latexmkrc` が既定ファイル・LuaLaTeX・BibTeX・SyncTeX を設定する。掃除は `make clean` または `latexmk -C` で行う。

**実行環境について：** 使用環境の既存 TeX エンジンは LuaHBTeX 1.18.0 だが、検索データベース・format・LuaTeX-ja が欠けていたため、同じエンジンに対応する TeX Live/Debian の配布パッケージを一時的な TeX ツリーに展開して補った。LuaTeX-ja は20250208。原稿に環境固有パスや代替フォントを埋め込まず、標準的な TeX Live 環境では上のコマンドだけで再生成する。環境修復用のパッケージ・キャッシュは研究資産ではなく、bundleに含めない。

**組版・表示の確認状態：** v1.2 は LuaLaTeX・BibTeX・latexmk による組版が成功し、最終PDFは **33頁**、SyncTeXも生成された。LaTeX の未解決参照・引用、overfull/underfull box、missing character は検出されなかった。字体の Font Info は警告ではない。未解決の参照・引用、LaTeX warning、overfull/underfull box、missing character はない。日本語の italic 指定に対する Font Info は直立字体を維持する通知であり、文字欠落ではない。ページ画像の全体配置を点検し、レビュー・相対分類・モジュライの主要頁と最終調整した頁を拡大して、文字・数式の欠け、重なり、式番号との衝突がないことを確認した。

## 5. 配布一式と反映の確認

**現在の状態：** v1.2 の原稿・PDF・bundle・検算の状態をそれぞれ確定する。GitHub の反映状態は操作完了後に remote `main` を確認し、反映失敗時には正確にその旨を記す。

文書内のローカル参照、TeX の `input`・label・citation key、必要ファイルの存在を確認する。GitHub へは現行のソースと再現資産を通常コミットで反映し、リモートの commit を確認する。GitHub Actions は使わない。

研究継続用bundleには、一つのルートディレクトリの下に、Gitで追跡する現行ファイルと、組版済みの `poisson-del-pezzo.pdf` を置く。PDFは `make pdf` の出力をコピーするもので、Gitでは追跡しない。旧版ZIP、旧原稿、Git履歴、環境修復用ファイル、組版中間生成物・ログを含めない。生成時にZIPのCRCと、各収録ファイルが確認済みのソース・PDFと一致することを確認する。

原稿生成、数学的点検、記号検算、組版、GitHub反映、配布用ファイルの保存は別々の状態として確認する。一つの成功を別の成功の証拠とはしない。
