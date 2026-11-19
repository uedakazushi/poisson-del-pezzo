# 研究方針：del Pezzo manifold の Poisson 構造

**2026-11-20（JST） / v1.2。再開時に最初に読む。**

**現在の反映状態：** v1.2 の現行ソース・検算コード・PDFをこの一式に保持する。GitHub `main` への反映は、操作の成否とリモート HEAD を独立に確認する。更新に失敗した場合は、この一式を正本の復旧資産とし、失敗を明記する。

続いて [研究ノート](research/research_notes.md)、[論文](poisson-del-pezzo.tex)、[検証・再現手順](docs/reproduction.md) を読む。以下の一般原則と、本研究に固有の計画を分けて記載する。

## A. 研究一般の原則と保存許可

1. **目標と方針。** 数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究全体の価値を最大化する。重要な変更では現在の理由と元の目標の解決済み・未解決部分を簡潔に整理し、有効な方針として書き換える。変更履歴を積み上げない。
2. **主張の確実性。** 証明済み、追加仮定付き、証明未完成、予想、計算的観察を区別する。仮定、依存、証明所在、未解決箇所を明記する。原稿の証明、今回の点検、実行した計算を別の状態とする。誤りは依存結果と関係する要約・方針にも反映し、有用な反例や障害はノートへ整理する。既知結果と本研究の成果、新規性未確認を区別する。
3. **先行研究。** 主要な主張の一次資料を読み、既存結果の仮定・範囲と本研究の貢献を Introduction で比較する。未確認の内容・書誌情報を推測しない。必要な識別子・参照箇所を保持するが、外部PDFや検索結果を大量収録しない。
4. **公表用論文。** 原則として日本語 LuaLaTeX を用い、十分な証明と明確な仮定を備える。現在の結果を理解しやすい順に統合し、数学的価値に応じて分割・統合する。有効で公表価値のある成果・証明を軽量化のために削らない。未完成原稿を完成と扱わない。
5. **研究ノート。** 現在有効な着想、補題、例、計算、反例、本質的な障害、文献比較を整理する。日誌・実況・全試行履歴・重複説明は収録しない。再取得が難しい情報は保持する。論文にある完全な証明は再掲せず参照する。
6. **研究再開。** 現行の一式から目標・到達点・核心・次の着手方法を理解できるようにする。必要な知識を会話だけに残さず、記法・ファイル名・参照・主張の状態を整合させる。
7. **bundle の軽量化。** 方針・ノート・論文と必要なソース、PDF、文献、コード、入力、証明書、再現手順だけを保持する。旧版ZIP、旧稿、バックアップ、ログ、編集記録、入れ子ZIP、キャッシュ、中間生成物は除外する。数学的内容と検証可能性は維持する。
8. **保存許可。** 研究の区切りごとに、追加の承諾を求めず研究継続用の一式を Library に保存する継続的な許可がある。本Gitプロジェクトの編集上の正本は GitHub `main` とし、区切りでは、その現行ソース・再現資産と組版済みPDFから自己完結した現行bundleを作る。Libraryのbundleを独立に編集する二重の正本にはしない。既存Libraryファイルの削除は別操作であり、明示的な指示なしには行わない。日付・版を付け、生成、数学的点検、計算、組版、GitHub反映、Library保存はそれぞれ実際に確認した状態だけを報告する。

## B. 中心目標と達成基準

滑らかな複素 del Pezzo manifold の Poisson 構造を、次数による違いを保ちながら幾何学的に説明する。**現在の中心は、次数1・2の任意次元でのスキーム論的分類と、Poisson 構造付き多様体のモジュライである。** 次数3の cubic は `nc-cubic`、次数4の詳細分類は `poisson-22ci`・`nc-22ci` を正本とし、本repoでは共通する構成と相違点を研究する。

公表用原稿はルートの `poisson-del-pezzo.tex`。短い del Pezzo manifold のレビュー、固定対象の分類、葉・曲面退化、相対分類・モジュライ、無限小変形、形式量子化を一つの論理的な単位にまとめる。公表の達成基準は、中心定理の仮定と証明の完結、関連文献との具体的な差分、読者が検証・再生成できる原稿である。量子化の代数化や全非可換変形の網羅性を完成の前提にはしない。

固定した $X$ の分類を維持しながら、現在は **動く多様体の族と正確な商スタック**へ重点を置く。理由は、Jacobi イデアルの一致が無限小基底上でも有効であり、cohomology and base change と同変な貼り合わせによってモジュライへ進めるからである。座標付き相対分類、基本線束の twist、Deligne–Mumford 性までを本文で証明した。coarse moduli、コンパクト化、相対量子化の降下は別の未解決問題として残る。方針変更の履歴ではなく、以下を現在の計画とする。

## C. 現在の到達点と状態

記法：$n\geq2$、$-K_X=(n-1)H$、$d=H^n\in\{1,2\}$。`Pois_sch(X)` は固定した $X$ 上の Schouten 二次写像の零スキーム。$\mathcal D_{n,d}$ は基本偏極のクラスを持つ多様体のスタック、$\mathcal P_{n,d}$ は相対 Poisson 構造を加えたスタックである。基本線束のスカラー自己同型と、Poisson 構造のスカラー倍を区別する。

| 主張 | 仮定・依存・証明の所在 | 現在の状態 |
| --- | --- | --- |
| 全大域二重ベクトルの Casimir 表示 | 標準重み付きモデル。`lemma:weighted-vanishing`、`lemma:ambient-restriction`、`prop:casimir-representative` | 本文に証明。今回の相対化の入力として論理を点検 |
| 次数1は $\mathbb A^n$、次数2は Plücker cone | `thm:jacobi-scheme`。Jacobi 係数から各 Plücker 二次式を線型回収 | イデアル一致の証明を保持。厳密記号検算を再実行 |
| 相対二重ベクトル束と任意基底変換 | `lemma:universal-sections-base-change`、`prop:relative-bivectors`。proper perfect base change と明示的な普遍切断 | 非被約基底を含む証明を記載・独立点検 |
| 相対 Jacobi スキーム | `thm:relative-poisson`。勾配係数行列の最大小行列式で局所左逆を作る | $U_1\times\mathbb A^n$、$U_2\times\operatorname{Cone}\operatorname{Gr}(2,n+1)$。平坦性も証明 |
| 基本偏極類と無標識の族 | `lemma:fundamental-polarization-class`。Picard 層と $H^1(\mathcal O)=H^2(\mathcal O)=0$ | 任意基底上でクラスが一意。基本線束自体の大域的存在は要求しない |
| 族の標準形・群作用 | `lemma:family-normal-form`、`prop:coordinate-action` | 任意基底での相対切断環、残余群、方程式の変換因子を証明。符号・重みを記号検算 |
| 内在的な二重ベクトル束 | `prop:intrinsic-bivector-bundle` | $p_*\wedge^2T\simeq\wedge^{n-1}(p_*H)\otimes p_*(\omega^{-1}\otimes H^{-(n-1)})$。偏極の基底 twist が相殺 |
| Poisson モジュライ | `thm:poisson-moduli`、`lemma:no-vector-fields` | 有限型・既約の DM スタックを明示的商で構成。忘却射は affine、有限表示、平坦 |
| 次元・滑らかさ・射影化 | `cor:moduli-dimension`、`cor:projective-moduli` | 次数1は滑らか、次数2の $n\geq3$ は零切断の点で特異。射影化は局所 Grassmann 族の降下 |
| 多様体を動かした零点の二次障害 | `cor:relative-deformations` | $Q\wedge Q$ は方程式の変形で相殺できない。本文証明と記号検算 |
| 零切断の解消と特異点型 | `sec:singularities`、`thm:poisson-resolution`、`cor:moduli-singularity-types` | 次数2の零切断の blow-up は滑らかな相対 Grassmann tautological line の全空間。n=3 は超曲面、n≥4 は非 lci。標準単項式理論の既知結果から terminal を導く。新規性未確認 |
| 階数2・葉・曲面退化・形式量子化 | `sec:geometry`、`sec:surfaces`、`thm:formal-quantization` | 有効な既存の証明を現行論文に保持。量子化部分の全面的な再監査は今回の点検範囲外 |
| 曲面 potential・Rees・条件付き AS 拡大 | `sec:surface-potential`、`prop:central-as-extension` | 形式的存在と追加仮定下の AS 正則性を区別して保持 |
| 次数4との比較 | `research/dp4_comparison.md` | 比較用の知識・例を保持。次数4全体の全面的な独立監査はしていない |

**新規性の状態：** 曲面の点分類、三次元の集合論的分類は既知。Hong–Xu の曲面 Poisson cohomology による次数1・2の変形次元10・9も既知。本研究の任意次元・相対 Jacobi スキーム・同変降下の主張は証明を本文に置くが、優先権の包括的な確認は未了。[文献メモ](research/literature_notes.md) に一次資料の版・箇所と未確認点を置く。形式証明器による検証は行っていない。

## D. 次に着手する課題

### 1. 公表に向けた位置付けと中心定理の磨き上げ

レビューと Introduction における Fujita、Kuznetsov–Prokhorov、LPT、Mayanskiy、Hong–Xu との比較を基準に、任意次元での分類、スキーム構造、相対化、ambient lift の各主張の既知性を調査する。高次元 foliation と weighted hypersurface の参照先を辿る。現在の証明の価値は、検索で同じ結果を発見しなかったことだけから判断しない。

### 2. モジュライの幾何と coarse space

次の具体的な入口は、零切断の blow-up の下での安定化群と正規形の群作用 `eq:moduli-action-one/two` における stabilizer の計算である。二重被覆 involution は $\pi\mapsto-\pi$ と作用し、零点・非零点・射影化で役割が変わる。一般の stabilizer、自己同型が増える層、coarse space の局所構造を順に調べる。DM 性だけから separatedness、有限 inertia、coarse space の具体形を結論しない。必要な GIT 安定性や商の存在定理の仮定を個別に確認する。

達成基準は、対象スタックと coarse space の区別を保った具体的定理を得ること。相対 Grassmann 族が大域的に通常のベクトル束の Grassmann 束になるとは仮定しない。基本線束の大域的存在の障害と、すでに降下した bivector 束を区別する。

### 3. 境界と量子化

特異な del Pezzo 多様体を含めると、勾配行列の階数落ちと偏微分 Koszul 複体の非完全性が最初の障害となる。まず一つの孤立特異点を持つ標準模型で、どの係数回収が壊れるかを調べる。滑らかな族の定理を境界へ自動的に延長しない。

相対量子化では、中心元と formality の選択が群作用・降下と両立するかを検討する。有限表示の代数化、AS 正則性の非形式的 locus、全 `coh(X)` 変形の認識は後続課題である。次数4の高階数構造を踏まえ、全次数を同じ Grassmann cone とする方針は採らない。

## E. 構成・検証・再開

主原稿は `poisson-del-pezzo.tex`、本文の七つの section source は `papers/sections/`、文献は `references.bib`。現行の分類・量子化を削除せず、新しいレビュー・族・モジュライを本文の論理順に統合した。旧主原稿の重複は置かない。

生成 PDF は `make pdf` またはルートからの `latexmk` により `build/poisson-del-pezzo.pdf` に出力する。SyncTeX を有効にする。主要な厳密検算は `make verify`。具体的な依存、検証結果、実行環境の制約は [docs/reproduction.md](docs/reproduction.md) を参照する。

一式の正本は `uedakazushi/poisson-del-pezzo` の `main`。通常コミットで反映し、GitHub Actions を使わない。研究継続用bundleは、現行ソース、必要な検算と文献、および組版済みPDFを含む一つの自己完結した一式とし、Git履歴や旧版を含めない。
