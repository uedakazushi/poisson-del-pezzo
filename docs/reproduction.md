# 再現手順と検証範囲

2026-11-20（JST） / v1.3

## 1. 正本と必要なファイル

正本は GitHub `main` の現行ソースである。[主原稿](../papers/poisson-del-pezzo.tex) は `papers/sections/` の八つの TeX と [references.bib](../references.bib) を読み込む。分割ソースは `del-pezzo-review.tex`、`classification.tex`、`geometry.tex`、`families.tex`、`moduli.tex`、`coarse.tex`、`singularities.tex`、`quantization.tex`。[研究方針](../00_research_plan.md) と [研究ノート](../research/research_notes.md) から再開でき、旧原稿や過去の会話を必要としない。

生成 PDF、SyncTeX、組版の中間ファイル、検算の標準出力は `build/` に置き、Git の追跡対象から除外する。再現コードを残すので、大量の生成出力は収録しない。

## 2. 今回の数学的な点検

今回の点検範囲は、主として `papers/sections/coarse.tex` と `papers/sections/singularities.tex` の次の議論である。

- 滑らかな係数領域の affine 性、有限 stabilizer を持つ還元群の作用への Luna の定理の適用、有限対角・分離性・affine 粗空間の構成。
- 任意の固定 $X$ 上の一般非零 Poisson 構造が自己同型を消すこと、一般多様体の deck-only locus、射影化での $\mu_2$ と次数1の $A_4=0$ 上の $\mu_6$ の区別。
- 粗忘却射の平坦領域の等式 $\operatorname{Flat}(f)=f^{-1}(M_{n,d}^{\mathrm{sm}})$。基底の strong étale slice、有限群不変環の Cohen–Macaulay 性、粗ファイバーの被約化と次元、miracle flatness、正則性の平坦降下、平坦 locus の開性と Jacobson 性を点検した。
- 次数1の $\mu_6$ 模型の存在、基底と Poisson 束の同時 slice、共変加群の階数と最小生成元数による非平坦性、粗ファイバーの $(u)^3$ による厚み。固定対象の自己同型商と、粗忘却射の scheme-theoretic fiber を区別した。
- 被覆対合による相対粗空間の偶数 Veronese 表示、任意基底変換、もとの零切断への制限と粗側零切断の厚い逆像の区別。
- 元の錐の $\mathcal O(-1)$ と符号商の $\mathcal O(-2)$ による解消、方程式の指標を保持した同変降下、例外因子に沿う二乗根スタックの記述。
- 符号商の標準指数、discrepancy、canonical・terminal の判定、非局所完全交叉性を検出する Hilbert 関数と二次関係数。

主要な新しい議論には並行した独立の論理点検も行った。これは人が読める証明の点検であり、Lean 等による形式化ではない。引用した一般定理の全証明を独立に再証明したものでもない。一次文献の確認箇所と適用条件は [文献メモ](../research/literature_notes.md) に記載する。Poisson モジュライへの適用の新規性・優先権の包括的な確認は未了である。

固定対象の weighted Euler 列・Casimir 表示・Jacobi イデアル、非被約基底を含む相対分類、相対 Picard 層と基本偏極類、座標作用、内在的な線束の捻りについては、現行原稿の証明を入力として保持した。今回の作業でその全証明を再監査したとは扱わない。葉の幾何・曲面退化・形式量子化・条件付き AS 拡大、[次数4比較ノート](../research/dp4_comparison.md) の全面的な再監査も今回の点検範囲外である。下記の既存検算を再実行したことは、これらの一般的な証明の全面的検証とは異なる。

## 3. 厳密な記号検算

Python 3 と SymPy を用いる。今回の確認環境は **Python 3.12.14 / SymPy 1.14.0**。

```sh
python3 -m pip install -r requirements.txt
make verify
```

`make verify` は四つのスクリプトを順に実行し、今回すべて成功した。浮動小数点近似やランダム標本を用いない。

| スクリプト・対象 | 実行範囲 | 確認内容 | 結果 |
| --- | --- | --- | --- |
| `verify_jacobi.py`、次数1 | $n=2,3,5$ | Casimir 条件、Jacobi 恒等式49組 | 成功 |
| 同、次数2 | $n=2,3,4,5$ | Casimir 条件、Jacobiator69組、Plücker 係数回収 | 成功 |
| 同、零点の変形 | 四つの独立な $x$ 方向 | 階数4方向が一次では許され二次で障害を持つ | 成功 |
| `verify_families.py`、次数1の同変性 | $n=2$、方程式と $D$ の係数は独立記号 | 非対角行列による直接 pushforward と $t^{-1}AD$ の一致 | 成功 |
| 同、次数2の同変性 | $n=3$、方程式と $P$ の係数は独立記号 | 直接 pushforward と $b^{-1}(\wedge^2A)P$ の一致、Plücker 関係の変換 | 成功 |
| 同、対合・中央スカラー・二次障害 | 両模型、一般の $Q,R$ と一次勾配変化、$\varepsilon^3=0$ | 対合の符号、中央スカラーの自明性、二次項が方程式の変化と $R$ に依存しないこと | 成功 |
| `verify_cone.py`、元の錐 | $2\leq n\leq19$ | 次元・余次元・Plücker 二次式数・discrepancy の整数チェック | 成功 |
| 同、符号商 | 任意次元の記号恒等式、$3\leq m\leq8$ の独立な tableau 数え上げ | Hilbert 関数の次数2・4、二次関係数と余次元の差の因数分解、非lciの数値条件 | 成功 |
| `verify_coarse.py`、二変数六次形式 | 六点の最初の三点の像を全120通り列挙、有理数体上 | 指定六点集合を保つ射影変換が恒等元だけであること | 成功 |
| 同、粗ファイバーの冪零元 | $n=2$、五つの $u$ 変数、二つの $v$ 変数、$(u)^3$ の35生成元 | $c=u_0v_0^4$ の不変性、$c\ne0$、$c^2\ne0$、$c^3=0$ | 成功 |
| 同、共変加群 | $n=2$ の次数2単項式15個、$2\leq n\leq6$ の生成元数 | 重み合同条件、階数1加群に必要な最小生成元数の数値 | 成功 |

六点集合に対応する具体的な六次形式は

$$f_6=x_0x_1(x_0-x_1)(x_0-3x_1)(x_0-7x_1)(x_0-11x_1).$$

射影変換は相異なる三点の像で一意に決まるため、120通りの列挙はこの具体例の全射影対称性を尽くす。任意次元の自己同型群の一般論の代用ではない。

Jacobi の検算は独立な勾配と対称 Hessian を使い、族の検算は非対角座標変更について二重ベクトルの pushforward を直接計算する。錐と粗空間の検算は数式・有限証明書・冪零元を確認する。**スタックの構成、任意次元の分類、全平坦領域の定理、CM性、標準指数、同変降下そのものは計算だけで証明していない。** 一般の証明は本文に置く。

## 4. LuaLaTeX 組版とエディタ設定

TeX Live の LuaTeX、LuaTeX-ja、BibTeX、latexmk と Noto Serif CJK JP / Noto Sans CJK JP を用意する。主なパッケージは `fix-cm`, `amsmath`, `amssymb`, `amsthm`, `mathtools`, `bm`, `geometry`, `booktabs`, `longtable`, `array`, `hyperref`, `luatexja-fontspec`。今回のログで確認したエンジンは LuaHBTeX 1.18.0、LuaTeX-ja は2025-02-08である。管理実行環境のシステムTeXには不足があったため、一時的に補ったTeXツリーを有効にして実行した。標準環境では上記の依存を導入して再生成する。環境修復用のパッケージ・キャッシュは研究資産に含めない。

ルートから次のいずれかを実行する。

```sh
make pdf
latexmk
```

主ファイルは `papers/poisson-del-pezzo.tex`。`.latexmkrc` は `-cd` 相当の設定で主原稿のディレクトリを参照基準にし、LuaLaTeX・BibTeX・SyncTeXを指定する。出力はリポジトリ直下の `build/poisson-del-pezzo.pdf` と `build/poisson-del-pezzo.synctex.gz`。分割稿の root 指定と文献の相対パスは主原稿の配置に合わせる。原稿に実行環境固有の絶対パスを埋め込まない。掃除は `make clean` または `latexmk -C`。

**組版の確認状態：** v1.3 は LuaLaTeX・BibTeX・latexmk による組版が成功し、最終PDFは **48頁**、SyncTeXも生成された。ログで未解決参照・引用、LaTeX warning、overfull/underfull box、missing character は検出されなかった。字体の Font Info は警告とは区別する。

**表示の確認状態：** 全48頁のページ画像で全体配置を点検し、追加した主要定理・粗ファイバーの局所環・符号商の公式を含む頁は拡大して確認した。文字・数式の欠け、重なり、式番号との衝突は見つからなかった。

`.vscode/settings.json` にはプロジェクトの `.latexmkrc` を明示して実行する LaTeX Workshop レシピを置き、出力先を `build/` に統一する。`.vscode/extensions.json` は `james-yu.latex-workshop` を推奨する。同じレシピの引数を使った CLI 組版は成功し、`synctex view` で `coarse.tex` の入力行からPDFの29頁への前方対応も確認した。**VS Code UI上でのコンパイル操作・PDF表示・前方／逆方向SyncTeX操作は未検証**である。CLI実行、SyncTeXファイル生成、UI操作はそれぞれ別の検証として扱う。

## 5. 保存と反映の確認

GitHub管理段階のため、現行ソースと再現資産を通常コミットで `main` へ反映し、リモートのコミットと内容を確認する。PDFは再生成できる出力として追跡しない。force push、履歴改変、GitHub Actions の追加・起動は行わない。並行する変更を保持する。

保存前には Markdown のローカル参照、TeX の `input`・label・citation key、必要ファイル、ビルド・エディタ設定との整合を確認する。対象repoを保存した結果に基づいて [research-hub](https://github.com/uedakazushi/research-hub) の該当項目を更新し、対象repoの反映とhubの反映は別々に確認する。

Libraryへの定常的な二重保存やZIP作成は行わない。push失敗時の緊急保存、または明示的な依頼がある場合に限り、現行ソース・必要な入力と組版済みPDFを自己完結した一式として保存する。その場合にも旧版、Git履歴、ログ、組版中間生成物を含めず、ZIPを作るなら整合性を確認する。既存Libraryファイルを明示的な指示なしに削除しない。

原稿生成、数学的点検、記号検算、組版、画像確認、GitHub反映、hub更新、例外時のファイル保存は、それぞれ実際に確認した状態だけを報告する。
