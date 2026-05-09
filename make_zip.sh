if [ ! -f "Milestone2_TCH_The Unicorn of Hermione.pdf" ]; then
    echo "Laporan belum dimasukkan atau format penamaan salah! (nama file: \"Milestone2_TCH_The Unicorn of Hermione.pdf\")"
    exit 1
fi

zip "Milestone2_TCH_The Unicorn of Hermione.zip" *.sql schema/*.sql seed/*.sql *.pdf