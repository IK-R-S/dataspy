def metadata_image():
    try:
        print(f'\033[1;93mBRILHO (Valor): \033[1;32m {img.brightness_value}\n')
    except:
        print(f'\033[1;93mBRILHO (Valor): \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mESPAÇO DE CORES: \033[1;32m {img.color_space}\n')
    except:
        print(f'\033[1;93mESPAÇO DE CORES: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mCONFIGURAÇÕES DE COMPONENTES: \033[1;32m {img.components_configuration}\n')
    except:
        print(f'\033[1;93mCONFIGURAÇÕES DE COMPONENTES: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mCOMPRESSÃO: \033[1;32m {img.compression}\n')
    except:
        print(f'\033[1;93mCOMPRESSÃO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mDATA HORA: \033[1;32m {img.datetime}\n')
    except:
        print(f'\033[1;93mDATA HORA: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mDATA HORA DIGITALIZADA: \033[1;32m {img.datetime_digitized}\n')
    except:
        print(f'\033[1;93mDATA HORA DIGITALIZADA: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mDATA HORA ORIGINAL: \033[1;32m {img.datetime_original}\n')
    except:
        print(f'\033[1;93mDATA HORA ORIGINAL: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mVERSÃO EXIF: \033[1;32m {img.exif_version}\n')
    except:
        print(f'\033[1;93mVERSÃO EXIF: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mVALOR DE EXPOSIÇÃO: \033[1;32m {img.exposure_bias_value}\n')
    except:
        print(f'\033[1;93mVALOR DE EXPOSIÇÃO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mMODO DE EXPOSIÇÃO: \033[1;32m {img.exposure_mode}\n')
    except:
        print(f'\033[1;93mMODO DE EXPOSIÇÃO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mPROGRAMA DE EXPOSIÇÃO: \033[1;32m {img.exposure_program}\n')
    except:
        print(f'\033[1;93mPROGRAMA DE EXPOSIÇÃO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mTEMPO DE EXPOSIÇÃO: \033[1;32m {img.exposure_time}\n')
    except:
        print(f'\033[1;93mTEMPO DE EXPOSIÇÃO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mFRAÇÃO DE ABERTURA DA LENTE (Quanto menor maior a abertura): \033[1;32m {img.f_number}\n')
    except:
        print(f'\033[1;93mFRAÇÃO DE ABERTURA DA LENTE (Quanto menor maior a abertura): \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mFLASH DA CÂMERA: \033[1;32m {img.flash}\n')
    except:
        print(f'\033[1;93mFLASH DA CÂMERA: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mVERSÃO DO FLASHPIX: \033[1;32m {img.flashpix_version}\n')
    except:
        print(f'\033[1;93mVERSÃO DO FLASHPIX: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mCOMPRIMENTO FOCAL: \033[1;32m {img.focal_length}\n')
    except:
        print(f'\033[1;93mCOMPRIMENTO FOCAL: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mCOMPRIMENTO FOCAL EM FILME DE 35mm: \033[1;32m {img.focal_length_in_35mm_film}\n')
    except:
        print(f'\033[1;93mCOMPRIMENTO FOCAL EM FILME DE 35mm: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mOBTENÇÃO: \033[1;32m {img.get}\n')
    except:
        print(f'\033[1;93mOBTENÇÃO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mOBTENÇÃO DE ARQUIVO: \033[1;32m {img.get_file}\n')
    except:
        print(f'\033[1;93mOBTENÇÃO DE ARQUIVO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mOBTENÇÃO DE MINIATURA: \033[1;32m {img.get_thumbnail}\n')
    except:
        print(f'\033[1;93mOBTENÇÃO DE MINIATURA: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mALTITUDE (gps): \033[1;32m {img.gps_altitude}\n')
    except:
        print(f'\033[1;93mALTITUDE (gps): \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mALTITUDE (gps) - referência: \033[1;32m {img.gps_altitude_ref}\n')
    except:
        print(f'\033[1;93mALTITUDE (gps) - referência: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mDATA DO GPS: \033[1;32m {img.gps_datestamp}\n')
    except:
        print(f'\033[1;93mDATA DO GPS: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mRUMO AO PONTO DE DESTINO DO GPS: \033[1;32m {img.gps_dest_bearing}\n')
    except:
        print(f'\033[1;93mRUMO AO PONTO DE DESTINO DO GPS: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mRUMO AO PONTO DE DESTINO DO GPS - referência: \033[1;32m {img.gps_dest_bearing_ref}\n')
    except:
        print(f'\033[1;93mRUMO AO PONTO DE DESTINO DO GPS - referência: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mERRO DE POSICIONAMENTO HORIZONTAL (gps): \033[1;32m {img.gps_horizontal_positioning_error}\n')
    except:
        print(f'\033[1;93mERRO DE POSICIONAMENTO HORIZONTAL (gps): \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mDIREÇÃO DE QUANDO A IMAGEM FOI CAPTURADA: \033[1;32m {img.gps_img_direction}\n')
    except:
        print(f'\033[1;93mDIREÇÃO DE QUANDO A IMAGEM FOI CAPTURADA: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mDIREÇÃO DE QUANDO A IMAGEM FOI CAPTURADA - referência: \033[1;32m {img.gps_img_direction_ref}\n')
    except:
        print(f'\033[1;93mDIREÇÃO DE QUANDO A IMAGEM FOI CAPTURADA - referência: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mVELOCIDADE DE QUANDO A IMAGEM FOI CAPTURADA (gps): \033[1;32m {img.gps_speed}\n')
    except:
        print(f'\033[1;93mVELOCIDADE DE QUANDO A IMAGEM FOI CAPTURADA (gps): \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mVELOCIDADE DE QUANDO A IMAGEM FOI CAPTURADA (gps) - referência: \033[1;32m {img.gps_speed_ref}\n')
    except:
        print(f'\033[1;93mVELOCIDADE DE QUANDO A IMAGEM FOI CAPTURADA (gps) - referência: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mHORA DO GPS: \033[1;32m {img.gps_timestamp}\n')
    except:
        print(f'\033[1;93mHORA DO GPS: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mCONTEÚDO EXIF: \033[1;32m {img.has_exif}\n')
    except:
        print(f'\033[1;93mCONTEÚDO EXIF: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mFORMATO DE INTERCÂMBIO .JPEG: \033[1;32m {img.jpeg_interchange_format}\n')
    except:
        print(f'\033[1;93mFORMATO DE INTERCÂMBIO .JPEG: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mCOMPRIMENTO DO FORMATO DE INTERCÂMBIO .JPEG: \033[1;32m {img.jpeg_interchange_format_length}\n')
    except:
        print(f'\033[1;93mCOMPRIMENTO DO FORMATO DE INTERCÂMBIO .JPEG: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mFABRICAÇÃO DE LENTE: \033[1;32m {img.lens_make}\n')
    except:
        print(f'\033[1;93mFABRICAÇÃO DE LENTE: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mMODELO DE LENTE: \033[1;32m {img.lens_model}\n')
    except:
        print(f'\033[1;93mMODELO DE LENTE: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mESPECIFICAÇÃO DA LENTE: \033[1;32m {img.lens_specification}\n')
    except:
        print(f'\033[1;93mESPECIFICAÇÃO DA LENTE: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mMODO DE EDIÇÃO: \033[1;32m {img.metering_mode}\n')
    except:
        print(f'\033[1;93mMODO DE EDIÇÃO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mMODELO DA MÁQUINA: \033[1;32m {img.model}\n')
    except:
        print(f'\033[1;93mMODELO DA MÁQUINA: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mORIENTAÇÃO: \033[1;32m {img.orientation}\n')
    except:
        print(f'\033[1;93mORIENTAÇÃO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mSENSIBILIDADE DE FOTOGRAFIA: \033[1;32m {img.photographic_sensitivity}\n')
    except:
        print(f'\033[1;93mSENSIBILIDADE DE FOTOGRAFIA: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mDIMENSÃO DO EIXO X (Em pixels): \033[1;32m {img.pixel_x_dimension}\n')
    except:
        print(f'\033[1;93mDIMENSÃO DO EIXO X (Em pixels): \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mDIMENSÃO DO EIXO Y (Em pixels): \033[1;32m {img.pixel_y_dimension}\n')
    except:
        print(f'\033[1;93mDIMENSÃO DO EIXO Y (Em pixels): \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mUNIDADE DE RESOLUÇÃO: \033[1;32m {img.resolution_unit}\n')
    except:
        print(f'\033[1;93mUNIDADE DE RESOLUÇÃO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mTIPO DE CAPTURA DE CENA: \033[1;32m {img.scene_capture_type}\n')
    except:
        print(f'\033[1;93mTIPO DE CAPTURA DE CENA: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mTIPO DE CENA: \033[1;32m {img.scene_type}\n')
    except:
        print(f'\033[1;93mTIPO DE CENA: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mMÉTODO DE DETECÇÃO: \033[1;32m {img.sensing_method}\n')
    except:
        print(f'\033[1;93mMÉTODO DE DETECÇÃO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mVELOCIDADE DO OBTURADOR DA CÂMERA: \033[1;32m {img.shutter_speed_value}\n')
    except:
        print(f'\033[1;93mVELOCIDADE DO OBTURADOR DA CÂMERA: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mSOFTWARE USADO: \033[1;32m {img.software}\n')
    except:
        print(f'\033[1;93mSOFTWARE USADO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mÁREA DE ESTUDO: \033[1;32m {img.subject_area}\n')
    except:
        print(f'\033[1;93mÁREA DE ESTUDO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mTEMPO SUBESEC DIGITALIZADO: \033[1;32m {img.subsec_time_digitized}\n')
    except:
        print(f'\033[1;93mTEMPO SUBESEC DIGITALIZADO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mTEMPO SUBESEC ORIGINAL: \033[1;32m {img.subsec_time_original}\n')
    except:
        print(f'\033[1;93mTEMPO SUBESEC ORIGINAL: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mBALANÇO DE BRANCO: \033[1;32m {img.white_balance}\n')
    except:
        print(f'\033[1;93mBALANÇO DE BRANCO: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mRESOLUÇÃO EM X: \033[1;32m {img.x_resolution}\n')
    except:
        print(f'\033[1;93mRESOLUÇÃO EM X: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mRESOLUÇÃO EM Y: \033[1;32m {img.y_resolution}\n')
    except:
        print(f'\033[1;93mRESOLUÇÃO EM Y: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mPOSICIONAMENTO Y;C: \033[1;32m {img.y_and_c_positioning}\n')
    except:
        print(f'\033[1;93mPOSICIONAMENTO Y;C: \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mCoordenada (Latitude): \033[1;32m {img.gps_latitude}\n')
    except:
        print(f'\033[1;93mCoordenada (Latitude): \033[1;32m Não possui\n')
    try:
        print(f'\033[1;93mCoordenada (Longitude): \033[1;32m {img.gps_longitude}\n')
    except:
        print(f'\033[1;93mCoordenada (Longitude): \033[1;32m Não possui\n')