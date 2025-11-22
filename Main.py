from PDF_Reader import Read_From_PDF
from Input_Path import file_path
from Agent import Agent_Run
import asyncio

Text = Read_From_PDF(file_path)
async def main():
    await Agent_Run(Text)

if __name__ == "__main__":
    asyncio.run(main())
