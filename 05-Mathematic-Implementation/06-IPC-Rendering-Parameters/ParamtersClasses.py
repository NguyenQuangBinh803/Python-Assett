class DivAlignInfo:
    def __init__(self):
        divnum_x
        divnum_y
        MARK_DT
        divPoint[MAX_ALIGN_DIV][2]
        markNum[MAX_ALIGN_DIV]
        SCALE_T
        scale[MAX_ALIGN_DIV]

       # [S]  # 1453 多点アライメント対応
        MARK_DIST
        markDist[MAX_MARK_NUM]
        areaMarkInfo[MAX_MARK_NUM]# マーク情報配列(領域毎のマークID格納)
        markInfoIndex[MAX_ALIGN_DIV]# マーク情報インデックス(マーク情報配列の指定子)

        // [E]  # 1453 多点アライメント対応
        areaScaleMode# RPL_SCL_INDIVIDUAL | RPL_SCL_AVE_AREA | RPL_SCL_PLANE
        boardScaleMode