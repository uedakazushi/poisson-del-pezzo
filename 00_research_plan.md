# 研究方針：del Pezzo manifold の Poisson 構造

**2026-11-20（JST） / v1.3。再開時に最初に読む。**

**正本と入口：** GitHub `main` の現行ソース・検算コードを正本とする。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。生成PDFは再現可能な出力として `build/` に置き、追跡しない。pushとhub更新は別々にremoteの内容を確認する。

続いて [研究ノート](research/research_notes.md)、[論文](papers/poisson-del-pezzo.tex)、[検証・再現手順](docs/reproduction.md) を読む。以下の一般原則と、本研究に固有の計画を分けて記載する。

## A. 研究一般の原則と保存許可

1. **目標と方針。** 数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究全体の価値を最大化する。重要な変更では現在の理由と元の目標の解決済み・未解決部分を簡潔に整理し、有効な方針として書き換える。変更履歴を積み上げない。
2. **主張の確実性。** 証明済み、追加仮定付き、証明未完成、予想、計算的観察を区別する。仮定、依存、証明所在、未解決箇所を明記する。原稿の証明、今回の点検、実行した計算を別の状態とする。誤りは依存結果と関係する要約・方針にも反映し、有用な反例や障害はノートへ整理する。既知結果と本研究の成果、新規性未確認を区別する。
3. **先行研究。** 主要な主張の一次資料を読み、既存結果の仮定・範囲と本研究の貢献を Introduction で比較する。未確認の内容・書誌情報を推測しない。必要な識別子・参照箇所を保持するが、外部PDFや検索結果を大量収録しない。
4. **公表用論文。** 原則として日本語 LuaLaTeX を用い、十分な証明と明確な仮定を備える。現在の結果を理解しやすい順に統合し、数学的価値に応じて分割・統合する。有効で公表価値のある成果・証明を軽量化のために削らない。未完成原稿を完成と扱わない。
5. **研究ノート。** 現在有効な着想、補題、例、計算、反例、本質的な障害、文献比較を整理する。日誌・実況・全試行履歴・重複説明は収録しない。再取得が難しい情報は保持する。論文にある完全な証明は再掲せず参照する。
6. **研究再開。** 現行の一式から目標・到達点・核心・次の着手方法を理解できるようにする。必要な知識を会話だけに残さず、記法・ファイル名・参照・主張の状態を整合させる。
7. **現行一式の軽量化。** 方針・ノート・論文と必要なソース、文献、コード、入力、証明書、再現手順だけを保持する。旧版ZIP、旧稿、バックアップ、ログ、編集記録、入れ子ZIP、キャッシュ、中間生成物は追跡しない。数学的内容と検証可能性は維持する。Library段階のbundleには組版済みPDFも含める。
8. **保存許可と管理段階。** GitHub管理前は区切りごとに自己完結した現行bundleを承諾不要でLibraryへ保存する。ユーザーが本repoを指定した現段階では `main` が正本であり、通常コミットとmainへのpushを承諾不要で行う。15〜30分を目安に区切り、並行変更を保持する。force pushとGitHub Actionsの追加・起動は行わない。Libraryへの定常的な二重保存・ZIP作成は不要で、push失敗時の緊急保存か明示的依頼に限る。既存Libraryファイルは明示的指示なしに削除しない。
9. **原稿配置と再現可能性。** 主原稿は `papers/poisson-del-pezzo.tex`。research-hubの `papers/paper-template.tex`、`papers/README.md` とlatexmk・VS Code設定を参考にし、LuaLaTeX・latexmk・LaTeX WorkshopでPDFとSyncTeXを `build/` に生成する。改名時はinput・文献・root指定と全案内を更新する。日付・版、生成、証明点検、計算、組版、GitHub反映、緊急Library保存は別々の確認状態とする。
10. **hub更新義務。** 区切りには本repoの原稿・ノート・方針・READMEを先に保存し、続いてhubの該当項目へ到達点、確実性、障害、次の一手、依存、正本・再開先、実際の資料確認日を反映する。最新hubと並行変更を確認し、詳細todo・証明・履歴を重複させない。実質的変化なしの日付更新は不要。成果保存とhub更新の成否を別々に確認し、失敗時は未反映項目と理由を報告する。

## B. 中心目標と達成基準

滑らかな複素 del Pezzo manifold の Poisson 構造を、次数による違いを保ちながら任意次元で幾何学的に説明する。**現在の中心は、次数1・2の相対Jacobiスキーム、Poissonモジュライ、粗忘却射の幾何である。** 次数3は `nc-cubic`、次数4の詳細分類は `poisson-22ci`・`nc-22ci` を正本とし、本repoでは共通構成と相違点を扱う。

主たる公表用原稿は `papers/poisson-del-pezzo.tex`。del Pezzo manifoldの短いレビュー、固定対象の分類、葉・曲面退化、相対分類、モジュライと粗空間、特異点解消、形式量子化を論理順にまとめる。公表の達成基準は、主要定理の仮定と十分な証明、先行研究との差分、再生成可能な原稿である。非形式的量子化や全非可換変形の分類を、公表のために無条件に解くとは要求しない。

固定対象と族の分類を保持しながら、自己同型が粗モジュライへ与える影響を明示する段階へ進んだ。全滑らか領域の有限対角・affine粗空間を構成し、**粗忘却射の平坦領域は粗基底の滑らかな部分の逆像に等しい**ことを示す。次数1の $A_4=0$ の一般模型では、追加の $\mu_3$ により粗基底が特異となり、その上の全ファイバーで非平坦になる。零点での局所環と冪零構造まで明示した。これはスタック上の平坦忘却射と両立する。基底の特異層の全分類、全ての特殊ファイバーの構造、境界・量子化の降下は残る。

## C. 現在の到達点と確実性

記法：$n\ge2$、$-K_X=(n-1)H$、$d=H^n\in\{1,2\}$。基底スタックを $\mathcal D_{n,d}$、Poissonスタックを $\mathcal P_{n,d}$、それぞれの粗空間を $M_{n,d},N_{n,d}$ とする。$C_{1,n}=\mathbb A^n$、$C_{2,n}=\operatorname{Cone}\operatorname{Gr}(2,n+1)$。

| 主張 | 仮定・依存・証明所在 | 現在の状態 |
| --- | --- | --- |
| 固定 $X$ の全bivector、Jacobiイデアル、ambient lift | 標準重み付き模型、Euler/Koszul。`thm:main`、`thm:jacobi-scheme` | 既存本文の証明を入力。公式検算は本段階でも実行。全証明の再監査とは区別 |
| 相対分類・任意基底変換・内在的twist | `sec:families`、`prop:intrinsic-bivector-bundle` | 非被約基底を含む既存の証明を保持。粗空間の研究の入力 |
| 商スタックと平坦忘却射 | `thm:poisson-moduli`、`lemma:no-vector-fields` | 既存の群作用・有限stabilizerの証明を読解し、粗空間への適用を点検 |
| 全滑らか領域の有限対角・affine粗空間 | `lemma:affine-parameter-open`、`thm:affine-coarse-moduli`。明示的resultant、Luna I§4 p.90、III§1 p.97 | 本段階で完全な証明を記載・独立点検。DM性だけからの推測ではない |
| 粗忘却射の正確な平坦領域 | `thm:coarse-flat-locus`。Cohen–Macaulay性、定次元既約ファイバー、一般Poisson対の自己同型消滅、miracle flatness | 本段階で証明・独立点検。$\operatorname{Flat}(N\to M)=f^{-1}(M_{\mathrm{sm}})$ |
| 固定対象の一般非零Poisson対の自己同型消滅 | `prop:generic-poisson-stabilizer`。Poisson表現の忠実性 | 任意の固定 $X$ に成立。射影化の一般慣性は次数2で $\mu_2$、次数1は $A_4=0$ なら $\mu_6$、それ以外 $\mu_2$ |
| 一般多様体の自己同型と粗局所模型 | `prop:generic-deck-stabilizer`、`cor:deck-only-coarse-model`。次数1は初等証明、次数2はPoonen Theorem 1.6 | 被覆対合だけの非空稠密開部分を証明。その上は滑らかな因子と第二Veronese錐の積 |
| 被覆対合の相対粗空間 | `thm:relative-deck-coarse`。$R^{\mu_2}=R^{(2)}$、Reynolds射影、AOV | 任意基底変換と両立。非零部分は同型。追加自己同型の商を取る全粗空間と区別 |
| 零切断の解消・二乗根スタック | `thm:poisson-resolution`、`thm:resolution-root-stack`。標準的な錐のblow-up、Cadman | 相対粗側の法線束は $\mathcal O(-2)$、もとの法線は $\mathcal O(-1)$。線型化のtwistを保持 |
| 符号商の標準指数・特異点型 | `thm:sign-quotient-index`、`prop:sign-quotient-nonlci` | $r=n$（次数1）、$r=n+1$（次数2）として指数 $2/\gcd(2,r)$、discrepancy $r/2-1$。次数1曲面のみcanonical非terminal、その他terminal。次数1曲面以外は非lci。既知の錐の幾何の適用 |
| 次数1の非平坦・非被約ファイバーの明示模型 | `thm:coarse-nonflat-degree-one`、`cor:coarse-nonflat-entire-fiber`。$A_4=0$、一般六次 $f_6$、Aut $=\mu_6$ | 全 $n\ge2$ で証明。$(X,0)$ の像における粗ファイバーの完成局所環 $(\mathbb C[[u,v]]/(u)^3)^{\mu_6}$ と $c^2\ne0,c^3=0$ を明示 |
| 葉・曲面退化・形式量子化・条件付きAS拡大 | `sec:geometry`、`sec:surfaces`、`thm:formal-quantization`、`prop:central-as-extension` | 有効な既存本文を保持。量子化の全証明の再監査は本段階の範囲外 |
| 次数4との比較 | `research/dp4_comparison.md` | 比較用の公式・例・障害を保持。次数4全体の独立監査は未実施 |

**既知性と検証の区別：** 曲面の点分類、三次元の集合論的分類、Hong–Xuの曲面の変形次元10・9は既知。Lunaの商・slice、Poonenの超曲面自己同型、AOVのtame商、Cadmanのroot stack、標準的な錐の特異点理論も既知の入力である。本研究では相対Jacobi錐との同定と具体的群作用を用いて粗忘却射を記述する。高次元分類・相対化・粗忘却射に関する研究固有の新規性の包括的確認は未了。証明の読解、有限の記号検算、組版は別の確認であり、形式証明器は実行していない。

## D. 優先課題と具体的な入口

### 1. 粗基底の特異層を自己同型表現から記述する

粗忘却射の平坦領域は基底の滑らかな部分へ還元できた。次は $M_{n,d}$ の特異点を、$\operatorname{Aut}(X)$ の変形接空間への作用から具体化する。まず次数2で $x_0\mapsto-x_0$ を保つ四次形式

$$f_4=x_0^4+x_0^2q_2(x_1,\ldots,x_n)+q_4(x_1,\ldots,x_n)$$

の一般族を入口とする。$T_fU_2/\mathfrak g_2f$ の固有空間を任意次元で数え、残余自己同型の増大を区別した上で粗基底の正則性を判定する。Chevalley–Shephard–Toddを使うなら一次資料と反射の条件を確認する。個別次元の例だけを上位目標にしない。

### 2. 特殊ファイバーと解消の全粗空間への移行

一般の $X$ で粗ファイバーの**被約化**は $C_{d,n}/\operatorname{Aut}(X)$ だが、そのスキーム構造には基底のArtin厚みが残る。次数1の $\mu_6$ 模型の完全局所環を基準に、安定化群表現から冪零構造を再現する方法を一般化する。deck対合に関する相対粗解消とroot stackは構成済みだが、追加自己同型も除いた全粗空間でblow-upがどう振る舞うかは別途確認する。商とblow-upの自動的な可換性を仮定しない。

### 3. 公表用の位置付けと証明監査

Fujita、Kuznetsov–Prokhorov、LPT、Mayanskiy、Hong–Xuとの比較を維持し、任意次元・Jacobiイデアル・相対化・粗忘却射の各主張について引用先を追う。既知の一般論の適用、別証明、Poisson幾何への具体化、新しい分類を分けてIntroductionへ反映する。検索で同じ結果を発見しなかったことだけから新規性を断定しない。古い量子化の主張も、公表前に外部入力の仮定まで再監査する。

### 4. 境界と量子化

特異del Pezzoを含める最初の障害は勾配行列の階数落ちと偏微分Koszul複体の非完全性である。一つの孤立特異点を持つ標準模型から、係数回収の破綻を調べる。滑らかな全領域の定理を境界へ自動延長しない。

相対量子化では中心元・formalityの選択と群作用・降下の両立を研究する。有限表示への代数化、AS正則性の非形式的locus、全 `coh(X)` 変形の認識は後続課題。次数4の高階数構造を踏まえ、全次数を同じGrassmann錐で記述する方針は採らない。

## E. 構成・再現・再開先

- 主原稿：`papers/poisson-del-pezzo.tex`。八つの本文ソースは `papers/sections/`、書誌は `references.bib`。本文の重複や旧主原稿は置かない。
- 研究ノート：`research/research_notes.md`、先行研究：`research/literature_notes.md`。論文にある証明を全文再掲せず、結果・障害・再開先を示す。
- 組版：ルートの `latexmk` または `make pdf`。PDFとSyncTeXは `build/`。VS Code設定はresearch-hubの現行ひな形を参考に、移動後の参照へ合わせた。
- 検算：`make verify`。Jacobi、族の変換、錐・符号商のHilbert関数、粗ファイバーの厳密検算。具体的範囲と実行結果は `docs/reproduction.md`。
- 正本：`uedakazushi/poisson-del-pezzo` の `main`。区切りにresearch-hubも更新する。PDFは追跡せず、Libraryへの定常的二重保存・ZIP生成は行わない。
